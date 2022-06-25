
import random
import requests
from bs4 import BeautifulSoup
import sys, os


HEADER = '\033[95m'
GREEN = '\033[92m'
RED = '\033[91m'
GRAY = '\033[30m'
BOLD = '\033[1m'
ENDC = '\033[0m'


class Istpian():
    
    def __init__(self ,cookie, url,options):
        self.cookie = cookie
        self.url = url
      
        self.subject = ''
        self.urlreq = ''
        
        self.input_random_values = options
       
        self.action = ''
        self.radio_inputs = []
        self.hidden_inputs = ''
        self.data = {}



   
    # get the page content and put it in the soup
    def get_the_page_content(self):
        response = requests.get(self.urlreq, cookies=self.cookie , verify=False)
        return response.text


    # get the page html and use beatifulSoup to access the content of the page
    # get the all input fieldes and put it into the self.input_field_list
    # get the form action of the istpian and put it into self.action 
    def deal_with_soup(self):
        try:
            soup = BeautifulSoup(self.get_the_page_content(), 'html.parser')

            self.radio_inputs = soup.find_all('input', type='radio')

            self.action = self.radio_inputs[5].find_previous('form').get('action')

            self.hidden_inputs = self.radio_inputs[5].find_previous('form').findChildren('input', type='hidden')
        except Exception as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"{RED}Error Type :" , exc_type , " At File :" , fname , ' Line :' , exc_tb.tb_lineno)
            print("Exception : ", e)
            print(f"{GREEN}Are you sure you entered the write url [the url you enterd is '{self.urlreq}']")
            exit()

  
    # genrate the the data dictionary to be submited 
    def genrate_input_data(self):
        data = {}

        for input in self.radio_inputs:
            if type(self.input_random_values) == list:
                rand_idx = random.randrange(len(self.input_random_values))
           
                data[input.get('name')] = self.input_random_values[rand_idx]
            else:
                data[input.get('name')] = self.input_random_values
               
        for input in self.hidden_inputs:
            data[input.get('name')] = input.get('value')

        return data

    # start the istpian from here
    def fire(self):
        
        self.urlreq = self.url + self.subject
        self.deal_with_soup()
        self.data = self.genrate_input_data()
        r = requests.post(self.action, data=self.data, cookies=self.cookie,  verify=False)
        # print(r.text)
        print(r.status_code)
        print(GREEN +f"Istpian Is for {self.subject} Completed Successfully" + ENDC)
        