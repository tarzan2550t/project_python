from datetime import date
from file_manager import FileManager 


class SalesManager:
    def __init__(self):
        self.sales_path = 'sales.txt'
        self.FileManager = FileManager()

    def generate_sale_id(self):
        try:
            sales = self.FileManager.read_file(self.sales_path)
            if not sales:
                
                return 'S001'

            last_id = sales[-1]['sale_id'].strip()

            if not last_id:
                return 'S001'
            
            number = int(last_id[1:]) + 1

            return f'S{number:03d}'

        except FileNotFoundError:
            return 'S001'
    
    def add_sale(self):
        self.product_id = input('Enter product ID: ').upper()
        self.quantity = int(input('Enter quantity: '))
        products = self.FileManager.read_file('products.txt')
        for product in products:
            if product['id'] == self.product_id:
                self.price = float(product['price'])
                break
            else:
                print('Product not found!')
                return
        self.sale_date = date.today()
        
        sales = {'sale_id':self.generate_sale_id() , 'product_id':self.product_id , 'quantity':self.quantity ,'unit_price':self.price  , 'date':self.sale_date  }
        datas = ','.join(str(value) for value in sales.values())
        self.FileManager.append_file(self.sales_path , datas)

