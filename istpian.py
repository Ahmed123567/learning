import re
import random
import argparse
import requests
from bs4 import BeautifulSoup

HEADER = '\033[95m'
GREEN = '\033[92m'
RED = '\033[91m'
GRAY = '\033[30m'
BOLD = '\033[1m'
ENDC = '\033[0m'


def banner():
    print(
        HEADER +
        """
        ██╗███████╗████████╗██████╗ ██╗ █████╗ ███╗   ██╗
        ██║██╔════╝╚══██╔══╝██╔══██╗██║██╔══██╗████╗  ██║
        ██║███████╗   ██║   ██████╔╝██║███████║██╔██╗ ██║
        ██║╚════██║   ██║   ██╔═══╝ ██║██╔══██║██║╚██╗██║
        ██║███████║   ██║   ██║     ██║██║  ██║██║ ╚████║
        ╚═╝╚══════╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
        """+RED+"""made by name
    """ + ENDC)


def arguments():
    parser = argparse.ArgumentParser(description='file istpian form')
    parser.add_argument('-u', '--url', help='please enter url', required=True)
    parser.add_argument('-op', '--options', nargs='+',
                        help='please enter options', required=True)
    parser.add_argument('--cookie', help='please enter cookies')
    return parser.parse_args()


def is_tanta(url):
  #  https://eng.tanta.edu.eg/
    is_tanta_unvirsty = re.search('https://.*/', url)

    if is_tanta_unvirsty != "https://eng.tanta.edu.eg/":
        print(RED + "\t\t\t Sorry It Must Be Tanta Universty " + ENDC)
        exit()


def cookie_array(cookie):
    cookie_name = cookie.split('=')[0]
    cookie_value = cookie.split('=')[1]

    cookie_list = [cookie_name, cookie_value]

    return cookie_list


def cookie_file():
    cookie_file = open('cookie.txt', 'r')
    cookie = cookie_file.read()
    cookie_list = cookie_array(cookie)

    return cookie_list


def get_the_page_content(url, cookies):
    response = requests.get(url, cookies=cookies)
    return response.text


def get_the_input_data(input_list, input_value):
    data = {}

    for input in input_list:
        rand_idx = random.randrange(len(input_value))
        random_value = input_value[rand_idx]

        if input.get('type') == 'checkbox':
            data[input.get('name')] = random_value

        if input.get('name') == '_token':
            data['_token'] = input.get('value')

    return data


def submit_form(action, data, cookie):
    r = requests.post(action, data=data, cookies=cookie)
    print(r.text)
    print(GREEN + "Istpian Is Completed Successfully" + ENDC)


def start():
    banner()
    args = arguments()
    url = args.url
    options = args.options
    cookie = args.cookie
    # is_tanta(url)

    if cookie == None:
        cookie_split = cookie_file()
    else:
        cookie_split = cookie_array(cookie)

    cookies = {}
    cookies[cookie_split[0]] = cookie_split[1]

    soup = BeautifulSoup(get_the_page_content(url, cookies), 'html.parser')

    data = get_the_input_data(soup.find_all('input'), options)

    submit_form(soup.form.get('action'), data, cookies)


if __name__ == "__main__":
    start()
