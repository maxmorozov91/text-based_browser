import os
import requests
from collections import deque
from sys import argv

DIRECTORY = argv[1]
EXIT = "exit"
BACK = "back"


def transform_url_short(url: str) -> str:

    for i in range(1, len(url)):
        if url[-i] == ".":
            short_url = url[:len(url) - i]
            return short_url


def transform_url_long(url: str) -> str:

    if not url.startswith("https://"):
        url = "https://" + url

    return url


def download_page(_downloaded_pages: set, directory: str, _content: str, url: str) -> set:

    page_name = transform_url_short(url)

    file_name = directory + "/" + page_name + ".txt"

    with open(file_name, "w") as file:
        file.write(_content)

    _downloaded_pages.add(page_name)

    return _downloaded_pages


def get_downloaded_page(directory: str, page_name: str) -> str:

    file_name = directory + "/" + page_name + ".txt"

    with open(file_name, "r") as file:
        content = file.read()

    return content


def make_directory(_path: str):
    
    if not os.path.exists(_path):
        os.mkdir(_path)


def go_back(_viewed_pages: deque) -> deque:

    if len(_viewed_pages):
        print(_viewed_pages.pop())

    return _viewed_pages    


def get_content(url: str):

    r = requests.get(transform_url_long(url))

    return r.text


def main(path: str):

    content = ""
    downloaded_pages = set()
    viewed_pages = deque()

    make_directory(path)

    while True:

        user_input = input()
        
        if user_input == EXIT:
            break

        elif user_input == BACK:
            viewed_pages = go_back(viewed_pages)
            continue
        
        elif user_input in downloaded_pages:
            viewed_pages.append(content)
            content = get_downloaded_page(path, user_input)

        else:
            viewed_pages.append(content)
            content = get_content(user_input)
            downloaded_pages = download_page(downloaded_pages, path, content, user_input)

        print(content)

 
if __name__ == "__main__":
    main(DIRECTORY)
