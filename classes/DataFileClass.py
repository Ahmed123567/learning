
RED = '\033[91m'
ENDC = '\033[0m'

import re


class DataFile():

    def __init__(self,path):
        self.path = path
        self.__data = self.__read_file()
        self.dictionary = {}
        self.keys = []

   #read the whole file and cache it in the self.__data dictionary
   #executed when the object is created
    def __read_file(self):
      
        try:
            text_file = open(self.path, 'r')
       
            lines = text_file.readlines()
            text_file.close()

            var_and_val = {}
            
            
            for line in lines:
                if line.find(':=') != -1 :
                    var_and_val[line.split(':=',1)[0]] =self.__check_for_list(line.split(':=',1)[1].replace('\n',''))
        
        except Exception as e :
            print(e)
            exit()
        
        return var_and_val

    def dict_algo(self,value):
        if value[0] == '{' and value[-1] == '}' and value.count('{')==1: 
            dictionary2 = {}
            dictionary2[value[1:-1].split(':')[0]] =  value[1:-1].split(':')[1]
            i=0
            d={}
            for key in keys[::-1]:
                if i == 0:
                    dictionary[key] = dictionary2
                else:    
                    dictionary[key] = d[f'di{i}'] 
                
                i = i+1
                d[f"di{i}"] = dictionary
         
        elif value[0] == '{' and value[-1] == '}':
            keys.append(value[1:-1].split(':',1)[0])

            dict_algo(value[1:-1].split(':',1)[1])

        return dictionary[keys[0]]


    def __check_for_list(self, value):
        
        if value.find(',') != -1:
            value = value.split(',')
  
        return value

   
    def get_all(self):

        return self.__data



    def get_val(self, varname): 
        
        if self.__data.get(varname) == None:
            print(f'{RED}Errore key {varname} key dosent exist{ENDC}')
            exit()

        return self.__data.get(varname)
        

    # insert if not exist update if exist 
    def update(self, var , val):

        self.__data[var] = val 
        
        return self
   
 
    def delete(self , var):
        
        self.__data.pop(var ,None)
        
        return self

   # write the self.__data dictionary in the file
   # can be chained to delete and update methods
   # Note:=> will remove all the comments in the file#
   # ex:=>(  file.delete('name').save()  )
    def save(self):
        try:
            text_file = open(self.path, 'w')
        except Exception as e:
            print(e) 
            exit()

        for key in self.__data:
            if type(self.__data[key]) == list :
                text_file.write(key  +  ':='  +  ','.join(self.__data[key])  + '\n')                
            else:
                text_file.write(key + ':=' + self.__data[key] + '\n')

            
dictionary = {}
keys = []
# def dict_algo(value):
#     if value[0] == '{' and value[-1] == '}' and value.count('{')==1 and len(keys) == 0:
#         dictionary2 = {}
#         dictionary2[value[1:-1].split(':')[0]] =  value[1:-1].split(':')[1]
#         return dictionary2

#     if value[0] == '{' and value[-1] == '}' and value.count('{')==1: 
#         dictionary2 = {}
#         dictionary2[value[1:-1].split(':')[0]] =  value[1:-1].split(':')[1]
#         i=0
#         d={}
#         for key in keys[::-1]:
#             if i == 0:
#                 dictionary[key] = dictionary2
#             else:    
#                 dictionary[key] = d[f'di{i}'] 
              
#             i = i+1
#             d[f"di{i}"] = dictionary
         
#     elif value[0] == '{' and value[-1] == '}':
#         keys.append(value[1:-1].split(':',1)[0])

#         dict_algo(value[1:-1].split(':',1)[1])
#     print(dictionary[keys[0]])
#     return dictionary[keys[0]]

# def parentDict(value):
#     for i in range(len(value.split(','))):
#         print(i)
#         print(len(value.split(','))-1)
#         if i == 0:
#            mainDict = dict_algo(value.split(',')[i].replace(' ', '') + '}')
#            print('this main one', mainDict)
#         elif i != len(value.split(',')) -1:
#             mainDict.update(dict_algo('{'+ value.split(',')[i].replace(' ', '')+ '}'))
#             print('this mian two',mainDict)
#         else:
#             print('{' + value.split(',')[i].replace(' ', ''))
#             mainDict.update(dict_algo('{' + value.split(',')[i].replace(' ', '')))
#             print('this main three', mainDict)

#     return mainDict        

# print(dict_algo("{name:{age:{hello:hell}}}")) 
# dicti = parentDict("{CS:programing,Mc:{math:{jfd:ejf}}, cc:noting}")

def dict_algo(value):
        if value[0] == '{' and value[-1] == '}' and value.count('{')==1: 
            dictionary2 = {}
            dictionary2[value[1:-1].split(':')[0]] =  value[1:-1].split(':')[1]
            i=0
            d={}
            for key in keys[::-1]:
                if i == 0:
                    dictionary[key] = dictionary2
                else:    
                    dictionary[key] = d[f'di{i}'] 
                
                i = i+1
                d[f"di{i}"] = dictionary
         
        elif value[0] == '{' and value[-1] == '}':
            keys.append(value[1:-1].split(':',1)[0])

            dict_algo(value[1:-1].split(':',1)[1])

        return dictionary[keys[0]]



dicti = dict_algo("{name:{age:{hello:hell}}}")
print(dicti['name']['name']['name']['name']['name']['name']['name'])

# print('final',dicti)