import sys
import os
from collections import deque


nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
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
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here

folder = sys.argv[1]
if not os.access(folder, os.F_OK):
    os.mkdir(folder)
page_stack = deque()
current_page = None
while True:
    url = input()
    if url == "exit":
        break
    elif "." in url:
        if url == "bloomberg.com":
            if current_page:
                page_stack.append(current_page)
            with open(f"{folder}/bloomberg", "w") as web_page:
                print(bloomberg_com)
                print(bloomberg_com, file=web_page)
            current_page = bloomberg_com
        elif url == "nytimes.com":
            if current_page:
                page_stack.append(current_page)
            with open(f"{folder}/nytimes", "w") as web_page:
                print(nytimes_com)
                print(nytimes_com, file=web_page)
            current_page = nytimes_com
        else:
            print("Error: Incorrect URL")
    elif url == "back":
        if page_stack:
            print(page_stack.pop())
    else:
        if os.access(f"{folder}/{url}", os.F_OK):
            with open(f"{folder}/{url}", "r") as web_page:
                print(web_page.read())
        else:
            print("Error: Incorrect URL")
