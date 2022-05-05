import random
import argparse
import requests
from bs4 import BeautifulSoup
from cookieClass import Cookies
from envClass import Env


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
        """+GREEN+"""made by ...
    """ + ENDC)


def arguments():
    parser = argparse.ArgumentParser(description='file istpian form')
    parser.add_argument('-u', '--url', help='please enter url')
   
    parser.add_argument('-op', '--options', nargs='+',
                        help='please enter options')
   
    parser.add_argument('-sub', '--subjects', nargs='+',
                        help='please enter options')
    
    parser.add_argument('-r', help="please enter the env file path" )

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--cookie', help='please enter cookies')
    group.add_argument('--path' , help='please enter the path to the file contains the cookie')
    return parser.parse_args()


def is_tanta(url):
    if url.find("tanta") == -1:
        print(RED + "\t\t\t Sorry It Must Be Tanta Universty " + ENDC)
        exit()


def get_the_page_content(url, cookies):
    response = requests.get(url, cookies=cookies, verify=False)
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
    r = requests.post(action, data=data, cookies=cookie,  verify=False)
    print(r.text)
    print(GREEN + "Istpian Is Completed Successfully" + ENDC)


def start():
    banner()
    args = arguments()

    if args.r :
        env = Env(args.r)
        args.url, args.options, args.sub  = env.get_val('url'),  env.get_val('options'),  env.get_val('subjects')
        CookieObject = Cookies(cookie=env.get_val('cookie'))
    else:
        if args.path != None:
            CookieObject = Cookies(path=args.path)
        else:
            CookieObject = Cookies(cookie=args.cookie)

   
    # is_tanta(args.url)

    cookies = CookieObject.cookie_formate()

    print(cookies)
 
    # soup = BeautifulSoup(get_the_page_content(args.url, cookies), 'html.parser')

    # data = get_the_input_data(soup.find_all('input'), args.options)

    # submit_form(soup.form.get('action'), data, cookies)


if __name__ == "__main__":
    start()
