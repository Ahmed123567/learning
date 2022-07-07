import sys,os

RED = '\033[91m'
ENDC = '\033[0m'
GREEN = '\033[92m'



class Cookies():


    def __init__(self,cookie=None, path=None):
        self.__cookie = cookie
        self.__path = path

    # takes input at this fomrate 'name=ahmed' return [ 'name' , 'ahmed']
    def cookie_unit(self,cookie):
        try:
            
            cookie_name = cookie.split('=',1)[0]
            cookie_value = cookie.split('=',1)[1]

        except Exception as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"{RED}Error Type :" , exc_type , " At File :" , fname , ' Line :' , exc_tb.tb_lineno)
            print("Exception : ", e)
            print(f'{GREEN}Cookie Formate : name=aname;age=31{ENDC}')
            exit()


        return [cookie_name, cookie_value]


    # read the cookie from the cookie.txt file and send to cookie_array method
    # this method works only if the cookie is not provided and the path is provided
    def cookie_file(self,path):
        try:
            
            # read the cookie form the file
            return open(path, 'r').read().replace("\n", "")

        except Exception as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"{RED}Error Type :" , exc_type , " At File :" , fname , ' Line :' , exc_tb.tb_lineno)
            print("Exception : ", e ,ENDC)
            exit()

        

    # take the inpute as ['name', 'ahmed' , 'job', 'eng' ] return {'name':'ahmed' , 'job':'eng' }
    def cookie_dictionary(self,cookie_array):
       
        cookies = {}
        cookie_array_len = len(cookie_array) 

        for i in range(0,cookie_array_len,2):
            cookies[cookie_array[i]] = cookie_array[i+1]

        return cookies


    # takes the whole cookie srting 'name=ahmed;job=eng' return ['name', 'ahmed' , job, 'eng']
    def cookie_array(self, cookie):
    
        if cookie == None:
           cookie = self.cookie_file(self.__path)
        
        cookies = cookie.split(';')
      
        cookie_list = []
        for cookie in cookies : 
            cookie_list += self.cookie_unit(cookie)

        return cookie_list

    #this where you should start reading the code
    
    def cookie_formate(self):
        cookie_list = self.cookie_array(self.__cookie)
    
        return self.cookie_dictionary(cookie_list)

