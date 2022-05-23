import argparse
from bs4 import BeautifulSoup
from classes.cookieClass import Cookies
from classes.DataFileClass import DataFile
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

    env = DataFile(args.r)
    print(env.get_all())
    CookieObject = Cookies(cookie = env.get_val('cookie'))
    
    istpian = Istpian(
                        cookie=CookieObject.cookie_formate() ,
                        url=env.get_val('url'),
                        options=env.get_val('options')
                    )
    
   
    if type(env.get_val('subjects')) == list:
        for subject in env.get_val('subjects'):
            istpian.subject = subject
            istpian.fire()
    
    else:
        istpian.subject = env.get_val('subjects')
        istpian.fire()
 

if __name__ == "__main__":
    start()
