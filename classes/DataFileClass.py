
RED = '\033[91m'
GREEN = '\033[92m'
BOLD = '\033[1m'
ENDC = '\033[0m'

import json
import re
import sys,os
class DataFile():

    def __init__(self,path):
        self.__path = path
        self.__data = self.__read_file()
       
   #read the whole file and cache it in the self.__data dictionary
   #executed when the object is created
    def __read_file(self):
      
        try:
            text_file = open(self.__path, 'r')
        except Exception as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"{RED}Error Type :" , exc_type , " At File :" , fname , ' Line :' , exc_tb.tb_lineno)
            print("Exception : ", e)
            exit()
        
        lines = text_file.readlines()
        text_file.close()

        var_and_val = {}
        
        
        for line in lines:
            if line.find(':=') != -1 :
                var_and_val[line.split(':=',1)[0]] =self.__check_for_types(line.split(':=',1)[1].replace('\n',''))
        
       
        
        return var_and_val

    def json(self, value):
        return json.loads(value)

    #this method check wether the value is 
    #dictionary or list or int or string
    def __check_for_types(self, value):

      
        if re.search('\{(.+:.+,?)+\}',value):
            return json.loads(re.search('{(.+:.+,?)+}',value).group())


        if re.search('\[.+,.+\]', value):
            dictstr = '{"list" :' + re.search('\[.+,.+\]', value).group() + "}"
            return json.loads(dictstr)['list']
        
        try:
            return int(value)
        except Exception:
            return value

  

   
    def get_all(self):

        return self.__data

    #return None if the the varname dosent exist
    def get_val(self, varname): 
     
        return self.__data.get(varname)
        

    # insert if not exist update if exist 
    def update(self, var , val):

        self.__data[var] = val 
        
        return self
   
 
    def delete(self , var):
        
        self.__data.pop(var ,None)
        
        return self


    def copy_to(self, file_path):
        original_path = self.__path
        self.__path = file_path
        self.save()
        self.__path = original_path


   # write the self.__data dictionary in the file
   # can be chained to delete and update methods
   # ex:=>(  file.delete('name').save()  )
   # Note:=> will remove all the comments in the file#
    def save(self):
      
        text_file = open(self.__path, 'w')
          
        for key in self.__data:
            if type(self.__data[key]) == list :
                dictlist = {'list' : self.__data[key]}
                text_file.write(key  +  ':='  + json.dumps(dictlist).replace('{"list":' , '').strip('}') + '\n')                
                continue

            if type(self.__data[key]) == dict:
                text_file.write(key + ':=' + json.dumps(self.__data[key]) + '\n')
                continue
            
            text_file.write(key + ':=' + str(self.__data[key]) + '\n')


