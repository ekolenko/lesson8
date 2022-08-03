import datetime
import os

class Log():
    def __init__(self, filename):
        self.filename = filename
        if self.isnew():
            f = open(self.filename,'w')
            f.close()



    def isnew(self):
       return not os.path.isfile(self.filename)
        

    
    def get_event(self, obj, str_in):

        time_stap = datetime.datetime.today()
        res_str = str(time_stap) + ' | ' + str(obj) + ' | ' + str_in +'\n'
        with open(self.filename, 'a') as f:
            f.write(res_str)

