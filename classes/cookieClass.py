import time


RED = '\033[91m'
ENDC = '\033[0m'


class Cookies():


    def __init__(self,cookie=None, path=None):
        self.cookie = cookie
        self.path = path

    # takes input at this fomrate 'name=ahmed' return [ 'name' , 'ahmed']
    def __cookie_unit(self,cookie):
        cookie_name = cookie.split('=',1)[0]
        cookie_value = cookie.split('=',1)[1]

        cookie_list = [cookie_name, cookie_value]
        return cookie_list


    # read the cookie from the cookie.txt file and send to cookie_array method
    def __cookie_file(self):
        try:
            cookie_file = open(self.path, 'r')
            self.cookie = cookie_file.read().replace("\n", "")

        except (FileNotFoundError , TypeError) as e :
            if self.path == None:
               print(RED+"Please provide a Cookie or Path"+ENDC)
            else: 
                print(f'{RED}Error: Path {self.path} dosnt exsit {ENDC}')
            exit()

        self.cookie_array()


    # take the inpute as ['name', 'ahmed' , 'job', 'eng' ] return {'name':'ahmed' , 'job':'eng' }
    def __cookie_dictionary(self,cookie_array):
       
        cookies = {}
        cookie_array_len = len(cookie_array) 

        for i in range(0,cookie_array_len,2):
            cookies[cookie_array[i]] = cookie_array[i+1]

        return cookies


    # takes the whole cookie srting 'name=ahmed;job=eng' return ['name', 'ahmed' , job, 'eng']
    def cookie_array(self):
    
        if self.cookie == None:
           self.__cookie_file()
        
        cookies = self.cookie.split(';')
      
        cookie_list = []
        for cookie in cookies : 
            cookie_list += self.__cookie_unit(cookie)

        return cookie_list


    def cookie_formate(self):
    
        cookie_array = self.cookie_array()

        cookies = self.__cookie_dictionary(cookie_array)

        return cookies



