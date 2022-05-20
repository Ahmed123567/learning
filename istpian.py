import random
import argparse
import requests
from bs4 import BeautifulSoup
from classes.cookieClass import Cookies
from classes.envClass import Env
from classes.istpianClass import Istpian


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
   
    parser.add_argument('-r', help="please enter the env file path", required=True)

    return parser.parse_args()


def start():
    banner()
    args = arguments()

    env = Env(args.r)
      
    CookieObject = Cookies(cookie = env.get_val('cookie'))
    cookies = CookieObject.cookie_formate()

    istpian = Istpian(cookies , env.get_val('uni')  , 'year' + env.get_val('year') , env.get_val('options'))

    istpian.trythis()

    istpian.fire()
 

if __name__ == "__main__":
    start()
