
import random
import requests
import sys, os

#this function can has any number of import statment 
#if the module is not installed it will install it
#you has to define the module name as global to make usable in the all code
keyboard_Interrupt = []
def import_or_install():
    try:
        global BeautifulSoup
        from bs4 import BeautifulSoup
        
    except ModuleNotFoundError as e:
        #if the pip install is colsed using ctrl+C will exit the code
        if e.msg.split(' ')[-1] in keyboard_Interrupt:
          exit()
       
        print(e)
        print(f"installing {e.msg.split(' ')[-1]}...")
        keyboard_Interrupt.append(e.msg.split(' ')[-1])

        os.system('pip3 install ' + e.msg.split(' ')[-1])
        import_or_install()

import_or_install()




HEADER = '\033[95m'
GREEN = '\033[92m'
RED = '\033[91m'
GRAY = '\033[30m'
BOLD = '\033[1m'
ENDC = '\033[0m'


class Istpian():
    
    def __init__(self ,cookie, url,options):
        self.__cookie = cookie
        self.__url = url
      
        self.__subject = ''
        self.__urlreq = ''
        
        self.__input_random_values = options
       
        self.__action = ''
        self.__radio_inputs = []
        self.__hidden_inputs = ''
        self.__data = {}



   
    # get the page content and put it in the soup
    def get_the_page_content(self):
        response = requests.get(self.__urlreq, cookies=self.__cookie , verify=False)
        return response.text


    # get the page html and use beatifulSoup to access the content of the page
    # get the all input fieldes and put it into the self.input_field_list
    # get the form action of the istpian and put it into self.action 
    def deal_with_soup(self):
        try:
            soup = BeautifulSoup(self.get_the_page_content(), 'html.parser')

            self.__radio_inputs = soup.find_all('input', type='radio')

            self.__action = self.__radio_inputs[5].find_previous('form').get('action')

            self.__hidden_inputs = self.__radio_inputs[5].find_previous('form').findChildren('input', type='hidden')

            self.__radio_inputs = self.__radio_inputs[5].find_previous('form').findChildren('input', type='radio')
      
        except Exception as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"{RED}Error Type :" , exc_type , " At File :" , fname , ' Line :' , exc_tb.tb_lineno)
            print("Exception : ", e)
            print(f"{GREEN}Are you sure you entered the write url [the url you enterd is '{self.__urlreq}']{ENDC}")
            exit()

  
    # genrate the the data dictionary to be submited 
    def genrate_input_data(self):
        data = {}

        for input in self.__radio_inputs:
            if type(self.__input_random_values) == list:
                rand_idx = random.randrange(len(self.__input_random_values))
                data[input.get('name')] = self.__input_random_values[rand_idx]
                continue
            
            data[input.get('name')] = self.__input_random_values
               
        for input in self.__hidden_inputs:
            data[input.get('name')] = input.get('value')

        return data

  
    def setSubject(self,subname):
        self.__subject = subname

    #load the data before fire
    def load(self):
        self.__urlreq = self.__url + self.__subject
        self.deal_with_soup()
        self.__data = self.genrate_input_data()
        

    
    # start the istpian from here
    def fire(self):
        self.load()
        r = requests.post(self.__action, data=self.__data, cookies=self.__cookie,  verify=False)
        # print(r.text)
        print(r.status_code)
        print(GREEN +f"Istpian Is for {self.__subject} Completed Successfully" + ENDC)
        