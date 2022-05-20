
class Env():

    def __init__(self,path):
        self.path = path
        self.__data = self.__read_file()

   #read the whole file and cache it in the self.__data dictionary
   # executed when the object is created
    def __read_file(self):
      
        try:
            text_file = open(self.path, 'r')
       
            lines = text_file.readlines()
            text_file.close()

            var_and_val = {}
            
            
            for line in lines:
                var_and_val[line.split(':',1)[0]] =self.__check_for_list(line.split(':',1)[1].replace('\n',''))
        
        except Exception as e :
            print(e)
            exit()
        
        return var_and_val

      
    def __check_for_list(self, value):
        
        if value.find(',') != -1:
            value = value.split(',')
  
        return value

   
    def get_all(self):

        return self.__data



    def get_val(self, varname): 

        return self.__data.get(varname) 


    # insert if not exist update if exist 
    # update self.__data dictionary
    def update(self, var , val):

        self.__data[var] = val 
        
        return self
   
   # delete from the self._data dictionary
    def delete(self , var):
        
        self.__data.pop(var ,None)
        
        return self

   # write the self.__data dictionary in the file
   #can be chained to delete and update methods
   # ex:=>(  file.delete('name').save()  )
    def save(self):
        try:
            text_file = open(self.path, 'w')
        except Exception as e:
            print(e) 
            exit()

        for key in self.__data:
            if type(self.__data[key]) == list :
                text_file.write(key  +  ':'  +  ','.join(self.__data[key])  + '\n')                
            else:
                text_file.write(key + ':' + self.__data[key] + '\n')

            



