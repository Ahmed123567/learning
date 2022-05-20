
import random
import requests
from bs4 import BeautifulSoup


HEADER = '\033[95m'
GREEN = '\033[92m'
RED = '\033[91m'
GRAY = '\033[30m'
BOLD = '\033[1m'
ENDC = '\033[0m'


class Istpian():
    
    def __init__(self ,cookie, uni, year, input_random_values):
        self.cookie = cookie
        self.uni = uni
        self.year = year

        # this supported uinversties dictionary contain 
        # url => 'the url of the istpian form'
        # formNum => 'it the third form in the page for example '
        # how to get the formNum write click the browser page => viewsourcepage then start count the forms 
        # until you reach the istpian form
        self.suportedUnis = {
            
            'tanta':{ 
                       'year3' :{'url':'http://www.google.com' , 'formNum' : 0}
                    }
            
            # you can add your universty url and formNum here 
            """
            'cairo':{
                    'year1':{'url':'????????????????????' , 'formNum' : ?},
                    'year2':{'url':'????????????????????' , 'formNum' : ?},
            }
            
            """ 

            }

        self.subject = ''
       
        self.is_suported_uni()

        self.url = self.suportedUnis[self.uni][self.year]['url'] + '/' + self.subject

        self.input_field_list = ''
        self.input_random_values = input_random_values
        self.action = ''
        self.deal_with_soup()
        self.data = self.genrate_input_data()

       
    def trythis(self):
        print(self.url)
        print(self.year)
        print(self.suportedUnis[self.uni][self.year]['formNum'])
        print(self.action) 
        # print(self.input_field_list)


    # get the page html and use beatifulSoup to access the content of the page
    # get the all input fieldes and put it into the self.input_field_list
    # get the form action of the istpian and put it into self.action 
    def deal_with_soup(self):
        
        soup = BeautifulSoup(self.get_the_page_content(), 'html.parser')

        self.input_field_list = soup.find_all('input')

        self.action = soup.find_all('form')[self.suportedUnis[self.uni][self.year]['formNum']].get('action')


    # check if the uni is suported
    # list all the suported unis and years
    def is_suported_uni (self):
        try:
            self.suportedUnis[self.uni]
        except Exception:
           
            print(self.uni + ' ' + self.year + ' is not suported')
           
            print(f'{GREEN}suported universties:{RED}')
            for key in self.suportedUnis:
                for key2 in self.suportedUnis[key]:
                    print( '\t' +key +'--->'+key2)
            exit()

    # get the page content and put it in the soup
    def get_the_page_content(self):
        try:
            response = requests.get(self.url, cookies=self.cookie, verify=False)
        except  Exception as e:
            print(e)
            exit()
        return response.text

    # genrate the the data dictionary to be submited 
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

    # start the istpian from here
    def fire(self):
        try:
            r = requests.post(self.action, data=self.data, cookies=self.cookie,  verify=False)
        except  Exception as e:
            print(e)
            exit()
        
        print(r.text)
        print(GREEN + "Istpian Is Completed Successfully" + ENDC)

      