from file_manager import FileManager
class Productmaneger: 
    def __init__(self):
        self.filemaneger = FileManager()

    def show_product(self):
        datas = self.filemaneger.read_file('products.txt')
        for data in datas : 
            print(f'{data['id']} , {data['product_name']} , {data['stock']} , {data['date']}')

# Productmaneger().show_product()