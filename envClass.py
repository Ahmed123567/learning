
class Env():

    def __init__(self,path):
        self.path = path
        self.__data = self.__read_file()

   
    def __read_file(self):
      
        text_file = open(self.path, 'r')
        lines = text_file.readlines()
        text_file.close()

        var_and_val = {}
        
        for line in lines:
            var_and_val[line.split(':',1)[0]] =self.__check_for_list(line.split(':',1)[1].replace('\n',''))

        return var_and_val

      
    def __check_for_list(self, value):
        
        if value.find(',') != -1:
            value = value.split(',')
  
        return value

   
    def get_all(self):

        return self.__data



    def get_val(self, varname): 

        return self.__data.get(varname) 


    def update(self, var , val):

        self.__data[var] = val 
        
        return self
   
   
    def delete(self , var):
        
        self.__data.pop(var ,None)
        
        return self

   
    def save(self):

        text_file = open(self.path, 'w')
        for key in self.__data:
            if type(self.__data[key]) == list :
                text_file.write(key  +  ':'  +  ','.join(self.__data[key])  + '\n')                
            else:
                text_file.write(key + ':' + self.__data[key] + '\n')

            



