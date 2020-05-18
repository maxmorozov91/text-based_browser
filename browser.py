import os
import requests
from sys import argv
from collections import deque

BLOOMBERG = "bloomberg.com"
NYTIMES = "nytimes.com"
DIRECTORY = argv[1]

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created 'soft' magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker's headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here


def transform_url(url: str) -> str:

    for i in range(1, len(url)):
        if url[-i] == ".":
            short_url = url[:len(url) - i]
            return short_url


def download_page(_downloaded_pages: set, directory: str, __pages: dict, url: str) -> set:

    page_name = transform_url(url)

    file_name = directory + "/" + page_name + ".txt"

    with open(file_name, "w") as file:
        file.write(__pages[url])

    _downloaded_pages.add(page_name)

    return _downloaded_pages


def get_downloaded_page(directory: str, page_name: str) -> deque:

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


def run_browser(_pages: dict, path: str):

    content = ""
    downloaded_pages = set()
    viewed_pages = deque()
    EXIT = "exit"
    BACK = "back"

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

        elif user_input in _pages:
            viewed_pages.append(content)
            content = _pages[user_input]
            downloaded_pages = download_page(downloaded_pages, path, _pages, user_input)

        else:
            print("error: url is not correct")
            continue

        print(content)


pages = {
    BLOOMBERG: bloomberg_com,
    NYTIMES: nytimes_com
}
 
run_browser(pages, DIRECTORY)
