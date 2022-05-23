import argparse
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

    print(env.get_all())
      
    CookieObject = Cookies(cookie = env.get_val('cookie'))
    cookies = CookieObject.cookie_formate()

    istpian = Istpian(
                        cookie=cookies ,
                        url=env.get_val('url'),
                        formNum=env.get_val('formNum'),
                        options=env.get_val('options')
                        )

    istpian.trythis()

    istpian.fire()
 

if __name__ == "__main__":
    start()
