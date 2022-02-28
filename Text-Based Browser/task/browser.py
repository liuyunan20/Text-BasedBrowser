import sys
import os
from collections import deque
import requests
from bs4 import BeautifulSoup


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
        break
    elif "https://" not in url:
        url = "https://" + url
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "Chrome/70.0.3538.77 Safari/537.36"
    try:
        page = requests.get(url, headers={'User-Agent': user_agent})
    except requests.exceptions.ConnectionError:
        print("Incorrect URL")
        continue
    if current_page:
        page_stack.append(current_page)
    file_name = url.replace("https://", "")
    soup = BeautifulSoup(page.content, "html.parser")
    text = []
    tags = soup.find_all(["p", "h1", "h2", "a", "ul", "ol", "li"])
    for tag in tags:
        tag_text = tag.text.strip()
        if tag_text:
            text.append(tag_text)
    with open(f"{folder}/{file_name}", "w", encoding="UTF-8") as web_page:
        if text:
            print(*text, sep="\n")
            print(*text, sep="\n", file=web_page)

    current_page = text
