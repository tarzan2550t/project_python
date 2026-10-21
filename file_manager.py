class FileManager :
    def read_file(self , pathname):
        with open(pathname , 'r' , encoding='utf-8') as file:
            datas = [data.strip().split(',') for data in file.readlines()]
            return datas
        
    def write_file(self , pahtname , datas):
        with open(pahtname , 'w' , encoding='utf-8') as file :
            file.writelines(datas)
            return 'successfully'

    def append_file(self , pahtname , data):
        with open(pahtname , 'a' ,encoding='utf-8') as file : 
            file.write(data+'\n')
            return 'successfully'
        

