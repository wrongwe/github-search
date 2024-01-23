import os
import shutil
import requests
import json
from tqdm import tqdm
from rich import print

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

    with open(file_path, 'wb') as file:
        for data in response.iter_content(1024):
            file.write(data)

def main():
    print_ascii_art()

    data_file = 'data.json'
    with open(data_file, 'r') as file:
        data = json.load(file)

    access_token = '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'
    tmp_dir = './temp_pocs'

    os.makedirs(tmp_dir, exist_ok=True)

    download_urls = []
    for html_url, repo_info in data.items():
        download_url = f"{html_url.replace('github.com', 'api.github.com/repos')}/zipball"  # 构造下载URL
        download_urls.append(download_url)

    for url in tqdm(download_urls, desc="Downloading……"):
        download_repo_zip(url, access_token, tmp_dir)

    # 将所有下载的 zip 文件打包到一个文件中
    shutil.make_archive('download', 'zip', tmp_dir)

    # 清理临时目录
    shutil.rmtree(tmp_dir)

if __name__ == '__main__':
    main()
