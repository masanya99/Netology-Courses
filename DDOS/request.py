import requests

N = 1000

list_urls = ['https://vk.com/',
             'https://www.youtube.com/',
             'https://www.netflix.com/',
             'http://www.fa.ru/',
             'https://github.com/']

for url in list_urls:
    for i in range(N):
        response = requests.get(url)
        print(f'{url} — #{i} — code: {response.status_code}')