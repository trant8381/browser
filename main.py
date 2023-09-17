import sys
import os
import requests
from bs4 import BeautifulSoup as bS
from colorama import Fore, Style

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
args = sys.argv
dir_name = args[1]
tabs_list = []
back = []
try:
    os.mkdir(f'{dir_name}')

except FileExistsError:
    print()
while True:
    url = input()
    if url == 'exit':
        break
    try:
        res = requests.get("https://" + url)
        soup = bS(res.content, 'html.parser')
        if res.status_code == 200:
            n = soup.findAll()
            j = []
            for char in n:
                if str(char).startswith("<a") and str(char).endswith("</a>"):
                    j += str(char.text) + Fore.BLUE
                    print(Style.RESET_ALL)
                else:
                    j += str(char.text)
            print("".join(j))
            file_name = ''
            for char in range(len(url) - 1, 0, -1):
                if url[char] == ".":
                    file_name = url[:char]
                    break
            with open(f'{dir_name}/{file_name}', 'a+') as dir_file:
                if len(dir_file.readlines()) > 0:
                    dir_file.close()
                    continue
                else:
                    dir_file.write(''.join(j))
                    dir_file.close()

    except requests.exceptions.ConnectionError:
        file_name = ""
        if os.path.exists(f'{dir_name}/{url}'):
            with open(f'{dir_name}/{url}', "r") as dir_file:
                print(dir_file.read().splitlines())
        else:
            print("Error: Incorrect URL")