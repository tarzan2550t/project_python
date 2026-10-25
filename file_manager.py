import csv
class FileManager :
    def read_file(self , pathname):
        with open(pathname, 'r', encoding='utf-8', newline='') as file:
            return list(csv.DictReader(file))
        

    def append_file(self , pathname ,data):
        with open(pathname  , 'a' ,encoding='utf-8') as file : 
            file.write(data+'\n') #ค่าที่ส่งมาเราแปลงเป็น string เเล้ว
            print('successfully')
        
    def read_file_id(self , id_pathname):
            with open(id_pathname, 'r', encoding='utf-8') as file:
               return  int(file.read().strip())

    def write_file_id(self , id_pathname , product_id):
        with open(id_pathname , 'w', encoding='utf-8') as file:
            file.write(str(product_id))
    