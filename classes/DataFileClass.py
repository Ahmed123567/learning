
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
        self.__data = self.read_file(self.__path)
       
    #read the whole file and cache it in the self.__data dictionary
    #executed when the object is created
    def read_file(self,path):
      
        try:
            lines = open(path, 'r').readlines()
        except Exception as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"{RED}Error Type :" , exc_type , " At File :" , fname , ' Line :' , exc_tb.tb_lineno)
            print(f"Exception : {e} {ENDC}")
            exit()
        
        var_and_val = {}
        
        
        for line in lines:
            if line.find(':=') != -1 and line.find('#') == -1 :
                var_and_val[line.split(':=',1)[0]] =self.translate_string(line.split(':=',1)[1].replace('\n',''))
        
        
        return var_and_val


    #this method check wether the value is 
    #dictionary or list or int or string
    def translate_string(self, value):

      
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
    def update(self, var, val):

        self.__data[var] = val 
        
        return self
   
    #update and delete methods has to be chained with save method to
    #make changes in the datafile
    #if you didn't chain it will only change the value in the data dict and wont be saved 
    def delete(self , var ):
        
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
            if isinstance(self.__data[key], list) :
                dictlist = {'list' : self.__data[key]}
                text_file.write(key  +  ':='  + json.dumps(dictlist).replace('{"list":' , '').strip('}') + '\n')                
                continue

            if isinstance(self.__data[key], dict):
                text_file.write(key + ':=' + json.dumps(self.__data[key]) + '\n')
                continue
            
            text_file.write(key + ':=' + str(self.__data[key]) + '\n')

        text_file.close()


