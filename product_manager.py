from file_manager import FileManager
class Productmaneger: 
    product_path = 'products.csv' 
    id_pathname = 'next_id.csv'
    file_manager = FileManager()


    def show_product(self):
        try:
            datas = self.file_manager.read_file(self.product_path)

            print("=" * 65)
            print(f"| {'ตารางสินค้า':^63} |")
            print("=" * 65)
            print(f"| {'ID':<8} | {'ชื่อสินค้า':<24} | {'ราคา':^12} | {'สต็อก':^13} |")
            print("-" * 65)

            for data in datas:
                print(
                    f"| {data['id']:<8} "
                    f"| {data['product_name']:<20} "
                    f"| {int(data['price']):^12,.2f} "
                    f"| {int(data['stock']):^12} |"
                )

            print("=" * 65)

        except FileNotFoundError:
            print('Not path file')


    def generate_id(self):
        try:
            current_id = self.file_manager.read_file_id(self.id_pathname)

            if current_id == 0:
                products = self.file_manager.read_file(self.product_path)
                product_id = max(
                    (int(p['id'][1:]) for p in products),
                    default=0
                ) + 1
            else:
                product_id = current_id

        except FileNotFoundError:
            products = self.file_manager.read_file(self.product_path)
            product_id = max(
                (int(p['id'][1:]) for p in products),
                default=0
            ) + 1

        self.file_manager.write_file_id(
            self.id_pathname,
            product_id + 1
        )

        return f'P{product_id:03d}'


    
    def add_product(self):
            self.product_name = input('Enter your product Name : ')
            self.product_price = input('Enter your product price : ')
            self.product_stock = input('Enter your product stock : ')
            product = {'id':self.generate_id() , 'product_name':self.product_name , 'price':self.product_price ,'stock':self.product_stock  }
            data = ','.join(str(value) for value in product.values())
            self.file_manager.append_file(self.product_path , data )
            
         