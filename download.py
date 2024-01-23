import os
import shutil
import requests
import json
import time
from rich import print
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

def print_ascii_art():
    ascii_art = """
    [bold cyan]Downloading [/bold cyan] [bold yellow]GitHub:https://github.com/wrongwe/github-search[/bold yellow]
    """
    print(ascii_art)

def download_repo_zip(url, token, target_dir):
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers, stream=True)
    repo_name = url.split('/')[-1]
    file_path = os.path.join(target_dir, f"{repo_name}.zip")

    max_retries = 3  # 最大重试次数
    retry_delay = 6  # 重试延迟时间（秒）

    for retry in range(max_retries):
        try:
            with open(file_path, 'wb') as file:
                total_size = int(response.headers.get('Content-Length', 0))
                with tqdm(total=total_size, unit='B', unit_scale=True, desc=file_path, ncols=80) as progress:
                    for data in response.iter_content(1024):
                        file.write(data)
                        progress.update(len(data))
            break  # 下载成功，跳出循环
        except Exception as e:
            print(f"An error occurred while downloading {url}: {str(e)}")
            if retry < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)  # 延迟重试

def main():
    print_ascii_art()

    data_file = 'data.json'
    with open(data_file, 'r') as file:
        data = json.load(file)

    access_token = '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'

    # 验证Access Token的有效性
    headers = {'Authorization': f'token {access_token}'}
    response = requests.get('https://api.github.com/user', headers=headers)
    if response.status_code == 200:
        print("Access Token有效，开始下载...")

        tmp_dir = './temp_download'
        os.makedirs(tmp_dir, exist_ok=True)

        download_urls = []
        for html_url, repo_info in data.items():
            download_url = f"{html_url.replace('github.com', 'api.github.com/repos')}/zipball"  # 构造下载URL
            download_urls.append(download_url)

        # 使用线程池进行多线程下载，并把它们存储在临时目录中
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(download_repo_zip, url, access_token, tmp_dir) for url in download_urls]
            for future in tqdm(as_completed(futures), total=len(futures), desc="Downloading"):
                pass  # 这里不做任何处理，tqdm 可以显示进度

        # 将所有下载的 zip 文件打包到一个文件中
        shutil.make_archive('download', 'zip', tmp_dir)

        # 清理临时目录
        shutil.rmtree(tmp_dir)
    else:
        print("Access Token无效或者过期，请检查并重新输入或者过段时间再用。")

if __name__ == '__main__':
    main()
