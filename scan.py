import os
import requests
import traceback
from tqdm import tqdm
import json

requests.packages.urllib3.disable_warnings()

class GithubClient:
    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': f'token {self.token}'}
    
    def verify_credentials(self):
        response = requests.get('https://api.github.com/user', headers=self.headers)
        if response.status_code == 200:
            return True
        else:
            return False
    
    def search_repositories(self, query, page=1, per_page=30):
        url = f"https://api.github.com/search/repositories?q={query}&page={page}&per_page={per_page}"
        r = requests.get(url, headers=self.headers)
        if r.ok:
            return r.json()
        else:
            raise Exception(f"Failed to fetch repositories: {r.text}")

def crawl_data_from_url(html_url, data, data_file, access_token):
    split_url = html_url.split('/')
    owner = split_url[3]
    repo = split_url[4]
    url = f"https://api.github.com/repos/{owner}/{repo}"
    
    headers = {'Authorization': f'token {access_token}'}
    response = requests.get(url, headers=headers)

    try:
        repo_info = response.json()
    except ValueError:
        print(f'Error parsing JSON data from: {url}')
        print(f'Response: {response.text}')
        return data

    minimal_info = {
        'name': repo_info.get('name'),
        'owner': repo_info.get('owner', {}).get('login'),
        'created_at': repo_info.get('created_at'),
        'last_push': repo_info.get('pushed_at'),
        'number_of_stars': repo_info.get('stargazers_count'),
        'number_of_forks': repo_info.get('forks_count'),
        'language': repo_info.get('language')
    }
    data[html_url] = minimal_info

    with open(data_file, 'w') as file:
        json.dump(data, file)

    return data

def main():
    root_path = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(root_path, 'data.json')
    data = {}
    html_urls = []
    
    access_token = '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'
    gc = GithubClient(access_token)

    if not gc.verify_credentials():
        print("Invalid API token. Please check your credentials.")
        return

    start_page = int(input("Enter the start page number: "))
    end_page = int(input("Enter the end page number: "))
    search_keyword = input("Enter the keyword you want to search: ")

    for page in range(start_page, end_page + 1):
        try:
            rs = gc.search_repositories(search_keyword, page=page, per_page=30)
            new_urls = [item['html_url'] for item in rs.get('items', []) 
                        if item.get('html_url')]
            new_urls = [url for url in new_urls if url not in data]
            if not new_urls:
                break
            html_urls += new_urls
            print(f'Got {len(new_urls)} new URLs at page {page}. Total URLs: {len(html_urls)}')
        except Exception as e:
            print(f"Failed to get URLs at page {page}. Reason: {e}")
            traceback.print_exc()

    print(f'[+] html_urls: {len(html_urls)}')

    for url in tqdm(html_urls, desc="Processing URLs"):
        try:
            data = crawl_data_from_url(url, data, data_file, access_token)
        except Exception as e:
            print(f"Failed to crawl data from URL: {url}. Error: {e}")

if __name__ == '__main__':
    main()
