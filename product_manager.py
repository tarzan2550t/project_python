from file_manager import FileManager
class Productmaneger: 
    product_path = 'products.txt'
    sales_path = 'sales.txt'

    def __init__(self):
        self.filemaneger = FileManager()

    def show_product(self):
        try:
            datas = self.filemaneger.read_file(self.product_path)
            for data in datas:
                print(f'{data['id']} , {data['product_name']} , {data['stock']} , {data['date']}')
        except FileNotFoundError :
            print('Not path file')
    
         