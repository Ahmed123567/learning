
import random
import requests
import sys, os

keyboard_Interrupt = []
# import or install 
while True:
    try:
        from bs4 import BeautifulSoup
        break
    except ModuleNotFoundError as e:
        #if the pip install is colsed using ctrl+C will exit the code
        if e.msg.split(' ')[-1] in keyboard_Interrupt:
          exit()
       
        print(f"{e.msg.split(' ')[-1]} is not installed ")
        ask_user = input(f"do you want to install {e.msg.split(' ')[-1]} [y / n] : ")
        
        keyboard_Interrupt.append(e.msg.split(' ')[-1])
        
        if ask_user.lower() != "n" and ask_user.lower() != "no":
            print(f"installing {e.msg.split(' ')[-1]}...")
            os.system('pip3 install ' + e.msg.split(' ')[-1])
        else:
            exit() 


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
        self.__options = options
  
        self.__subject = ''
        self.__urlreq = ''       
        self.__action = ''
        self.__radio_inputs = []
        self.__hidden_inputs = ''
        self.__data = {}



   
    # get the page content and put it in the soup
    def get_the_page_content(self, url , cookie ) :
        response = requests.get(url, cookies=cookie , verify=False)
        return response.text


    # get the page html and use beatifulSoup to access the content of the page
    # get the all input fieldes and put it into the self.input_field_list
    # get the form action of the istpian and put it into self.action 
    def __deal_with_soup(self):
        try:
            rad_indx = 15
            soup = BeautifulSoup(self.get_the_page_content(self.__urlreq, self.__cookie), 'html.parser')

            self.__radio_inputs = soup.find_all('input', type='radio')

            self.__action = self.__radio_inputs[rad_indx].find_previous('form').get('action')

            self.__hidden_inputs = self.__radio_inputs[rad_indx].find_previous('form').findChildren('input', type='hidden')

            self.__radio_inputs = self.__radio_inputs[rad_indx].find_previous('form').findChildren('input', type='radio')
      
        except Exception as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"{RED}Error Type :" , exc_type , " At File :" , fname , ' Line :' , exc_tb.tb_lineno)
            print("Exception : ", e)
            print(f"{GREEN}Are you sure you entered the write url [the url you enterd is '{self.__urlreq}']{ENDC}")
            exit()


    def is_list_of_strings(self, alist):
        return bool(alist) and all(isinstance(elem, str) for elem in alist)

  
    # genrate the the data dictionary to be submited
    # radio_inputs is alist of beatifulsoup input objects
    # or list of dicts with the key "name" ex:=> [{'name':'the input name'}, {'name':'the input name'},{'name':'the input name'}]
    # radio_inputs can also take just alist of the input field names ex:=>   ['ahmed','omar', 'sayed'] 
    # for other_inputs ex:=> [{'name':'hidden1','value':2},{'name':'hidden2', 'value':4}]
    def genrate_input_data(self,options, radio_inputs='' , other_inputs=''):
        data = {}
        
        # excute if the radio_unputs is list of strings to prebare the data
        # convert from ['ahmed','omar', 'sayed'] to [{'name':'ahmed'}, {'name':'omar'},{'name':'sayed'}]
        if self.is_list_of_strings(radio_inputs):
            radio_data={}
            radio_list=[]
            for item in radio_inputs:
                radio_data['name'] = item
                radio_list.append(radio_data.copy())
            radio_inputs = radio_list

       # this the main part of the function that genrate the data dict to be submitted
        for input in radio_inputs:
            if isinstance(options, list):
                rand_idx = random.randrange(len(options))
                data[input.get('name')] =options[rand_idx]
                continue
            
            data[input.get('name')] = options
               
        
        for input in other_inputs:
            data[input.get('name')] = input.get('value')

        return data

  
    def setSubject(self,subname):
        self.__subject = str(subname)

    #load the data before fire
    def __load(self):
        self.__urlreq = self.__url + self.__subject
        self.__deal_with_soup()
        self.__data = self.genrate_input_data(self.__options, self.__radio_inputs, self.__hidden_inputs)
        self.__hidden_inputs=''
        print(self.__data)

    
    # start the istpian from here
    def fire(self):
        self.__load()
        r = requests.post(self.__action, data=self.__data, cookies=self.__cookie,  verify=False)
        # print(r.text)
        print(r.status_code)
        print(GREEN +f"Istpian Is for {self.__subject} Completed Successfully" + ENDC)
        