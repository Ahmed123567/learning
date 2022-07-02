import argparse
from classes.cookieClass import Cookies
from classes.DataFileClass import DataFile
from classes.istpianClass import Istpian


HEADER = '\033[95m'
GREEN = '\033[92m'
DARK = '\033[90m'
RED = '\033[91m'
GRAY = '\033[30m'
BOLD = '\033[1m'
ENDC = '\033[0m'


def banner():
    print(
        HEADER +
       f"""
       {GRAY} ██╗███████╗████████╗██████╗ ██╗ █████╗ ███╗   ██╗
      {DARK}  ██║██╔════╝╚══██╔══╝██╔══██╗██║██╔══██╗████╗  ██║
        ██║███████╗   ██║   ██████╔╝██║███████║██╔██╗ ██║ 
        ██║╚════██║   ██║   ██╔═══╝ ██║██╔══██║██║╚██╗██║
    {GRAY}    ██║███████║   ██║   ██║     ██║██║  ██║██║ ╚████║
        ╚═╝╚══════╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝                    
        """+BOLD+GREEN+"""made by ...
    """ + ENDC)




def arguments():
    parser = argparse.ArgumentParser(description='finish the unvirsty istpian')
   
    parser.add_argument('-r', help="please enter the env file path", required=True)

    return parser.parse_args()




def start():
    banner()
    args = arguments()

    env = DataFile(args.r)
    
    CookieObject = Cookies(cookie=env.get_val('cookie'))
    
    istpian = Istpian(cookie=CookieObject.cookie_formate(),  url=env.get_val('url'), options=env.get_val('options') )
    
    # print(env.get_all())
    print(CookieObject.cookie_formate())
    # fire the istpian for each subject if it is alist of subjects
    if isinstance(env.get_val('subjects'), list):
        for subject in env.get_val('subjects'):
            istpian.setSubject(subject)
            istpian.fire()

    # if it is only one subject
    else:
        istpian.setSubject(env.get_val('subjects'))
        istpian.fire()

    # radio_list = [{'name':'ahmed'}, {'name':'omar'},{'name':'said'}]
    # hidden_list = [{'name':'_token', 'value':'this secret'}]
    # print(istpian.genrate_input_data( [1,2,3,4,5,6], radio_list, hidden_list))
 

if __name__ == "__main__":
    start()
