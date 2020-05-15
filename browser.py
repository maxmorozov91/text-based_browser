from sys import argv
import os

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


def is_url_correct(url: str) -> bool:

    global pages
  
    if url not in pages:
        print("error: url is not correct")
        return False

    return True


def transform_url(url: str) -> str:

    for i in range(len(url)):
        if url[-i] == ".":
            short_url = url[:len(url) - i]
            return short_url


def download_page(url: str):
    
    global pages
    global downloaded_pages
    global directory

    page_name = transform_url(url)

    file_name = directory + "/" + page_name + ".txt"

    with open(file_name, "w") as file:
        file.write(pages[url])

    downloaded_pages.add(page_name)


def show_new_page(url: str):
    
    global pages

    print(pages[url])


def show_downloaded_page(page_name: str):

    global directory

    file_name = directory + "/" + page_name + ".txt"

    with open(file_name, "r") as file:
        content = file.read()
        print(content)


pages = {
    "bloomberg.com": bloomberg_com,
    "nytimes.com": nytimes_com
}

downloaded_pages = set()

directory = argv[1]

if not os.path.exists(directory):
    os.mkdir(directory)


while True:

    user_input = input()

    if user_input == "exit":
        break
    
    if user_input in downloaded_pages:
        show_downloaded_page(user_input)
    
    else:
        if is_url_correct(user_input):
            show_new_page(user_input)
            download_page(user_input)
