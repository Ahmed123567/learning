
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


class Istpian():
    
    def __init__(self , cookie , uni , input_random_values):
        self.cookie = cookie
        self.uni = uni
        self.suportedUnis = {
            'tanta':{ 'url':'http://www.google.com' , 'formNum' : 3}
            }

        self.input_field_list
        self.input_random_values = input_random_values
        self.action
        self.deal_with_soup()
        self.data = self.genrate_input_data()

       

    def banner(self):
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

    def trythis(self):
        print(self.suportedUnis[self.uni]['url'])


    def deal_with_soup():
        
        soup = BeautifulSoup(get_the_page_content(self.suportedUnis[self.uni]['url'], self.cookie), 'html.parser')

        self.input_field_list = soup.find_all('input')

        self.action = soup.find_all('form')[self.suportedUnis[self.uni]['formNum']]





    def is_tanta(self):
        if self.suportedUnis[self.uni]['url'].find("tanta") == -1:
            print(RED + "\t\t\t Sorry It Must Be Tanta Universty " + ENDC)
            exit()


    def get_the_page_content(self):
        response = requests.get(self.suportedUnis['tanta']['url'], cookies=self.cookie, verify=False)
        return response.text


    def genrate_input_data(self):
        data = {}

        for input in self.input_field_list:
            rand_idx = random.randrange(len(self.input_random_values))
            random_value = self.input_random_values[rand_idx]

            if input.get('type') == 'checkbox':
                data[input.get('name')] = random_value

            if input.get('name') == '_token':
                data['_token'] = input.get('value')

        return data


    def submit_form(self):
        r = requests.post(self.action, data=self.data, cookies=self.cookie,  verify=False)
        print(r.text)
        print(GREEN + "Istpian Is Completed Successfully" + ENDC)

        

istpian = Istpian('hello:name', 'tanta')

istpian.trythis()