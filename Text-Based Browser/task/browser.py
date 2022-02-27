import sys
import os
from collections import deque
import requests


folder = sys.argv[1]
print(folder)
if not os.access(folder, os.F_OK):
    os.mkdir(folder)
page_stack = deque()
current_page = None
while True:
    url = input()
    if url == "exit":
        break
    elif url == "back":
        if page_stack:
            print(page_stack.pop())
    elif "https://" not in url:
        url = "https://" + url

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "Chrome/70.0.3538.77 Safari/537.36"
    page = requests.get(url, headers={'User-Agent': user_agent})

    if current_page:
        page_stack.append(current_page)
    file_name = url.replace("https://", "")
    with open(f"{folder}/{file_name}", "w", encoding="UTF-8") as web_page:
        print(page.text)
        web_page.write(page.text)
    current_page = page
