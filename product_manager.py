from file_manager import FileManager
class Productmaneger: 
    def __init__(self):
        self.filemaneger = FileManager()

    def show_product(self):
        data = self.filemaneger.read_file('product.txt')
        print(f'')