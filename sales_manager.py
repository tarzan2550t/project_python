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
        try:
            self.product_id = input('Enter product ID: ').strip().upper()
            self.quantity = int(input('Enter quantity: '))

            # ตรวจสอบจำนวนที่ต้องการขาย
            if self.quantity <= 0:
                print('Quantity must be greater than 0!')
                return

            # อ่านข้อมูลสินค้า
            products = self.FileManager.read_file('products.txt')

            # ค้นหาสินค้าจาก ID
            product_found = None

            for product in products:
                if product['id'].strip().upper() == self.product_id:
                    product_found = product
                    break

            if product_found is None:
                print('Product not found!')
                return

            # ตรวจสอบสต็อก
            stock = int(product_found['stock'])

            if self.quantity > stock:
                print(f'Not enough stock! Available: {stock}')
                return

            # ดึงราคาจากข้อมูลสินค้า
            self.price = float(product_found['price'])

            # คำนวณสต็อกคงเหลือ
            product_found['stock'] = str(stock - self.quantity)

            # บันทึกสต็อกใหม่ลง products.txt
            self.FileManager.write_file('products.txt', products)

            # สร้างข้อมูลการขาย
            self.sale_date = date.today()

            sales = {
                'sale_id': self.generate_sale_id(),
                'product_id': self.product_id,
                'quantity': self.quantity,
                'unit_price': self.price,
                'date': self.sale_date
            }

            # บันทึกการขายลง sales.txt
            datas = ','.join(str(value) for value in sales.values())
            self.FileManager.append_file(self.sales_path, datas)

            print(f"Stock remaining: {product_found['stock']}")
            self.show_receipt(sales)

        except FileNotFoundError:
            print('File not found! Please check your file paths.')

        except ValueError:
            print('Please enter a valid number for quantity or stock.')

    def show_receipt(self , data_sales):
        try:
            datas = [data_sales]
            for sale in datas:
  
                quantity = int(sale['quantity'])
                unit_price = float(sale['unit_price'])
                total = quantity * unit_price
                print()
                print('=' * 40)
                print(f"{'SALES RECEIPT':^40}")
                print('=' * 40)
                print(f"Sale ID   : {sale['sale_id']}")
                print(f"Date      : {sale['date']}")
                print('-' * 40)
                print(f"Product ID: {sale['product_id']}")
                print(f"Quantity  : {quantity}")
                print(f"Unit Price: {unit_price:,.2f} THB")
                print('-' * 40)
                print(f"{'TOTAL':<15} {total:>20,.2f} THB")
                print('=' * 40)
                print(f"{'Thank you for your purchase!':^40}")
                print('=' * 40)

        except FileNotFoundError:
            print('Sales file not found.')

    def show_sales(self):
        try:
            sales = self.FileManager.read_file(self.sales_path)

            if not sales:
                print('No sales records found.')
                return

            print('=' * 55)
            print(f"{'SALES REPORT':^55}")
            print('=' * 55)
            print(f"{'Sale ID':<10}{'Product ID':<15}{'Quantity':<10}{'Total':>15}")
            print('-' * 55)

            for sale in sales:
                sale_id = sale['sale_id']
                product_id = sale['product_id']
                quantity = int(sale['quantity'])
                unit_price = float(sale['unit_price'])
                total = quantity * unit_price

                print(
                    f'{sale_id:<10}'
                    f'{product_id:<15}'
                    f'{quantity:<10}'
                    f'{total:>12,.2f} THB'
                )
                print(f"Date: {sale['date']}")

            print('=' * 55)
            print('End of sales report')

        except FileNotFoundError:
            print('Sales file not found.')


    def daily_sales_report(self):
        try:
            day = input('Enter date (YYYY-MM-DD): ')
            sales = self.FileManager.read_file(self.sales_path)

            # เลือกเฉพาะรายการขายของวันที่ระบุ
            today_sales = [
                sale for sale in sales
                if str(sale['date']) == day
            ]

            print('\n' + '=' * 65)
            print(f"{'DAILY SALES REPORT':^65}")
            print(f"{'Date: ' + day:^65}")
            print('=' * 65)

            if not today_sales:
                print(f"{'No sales on this date.':^65}")
                print('=' * 65)
                return

            # หัวตาราง
            print(
                f"{'Sale ID':<10}"
                f"{'Product ID':<15}"
                f"{'Qty':>6}"
                f"{'Price':>15}"
                f"{'Total':>15}"
            )
            print('-' * 65)

            grand_total = 0
            total_quantity = 0

            # แสดงรายการขาย
            for sale in today_sales:
                sale_id = sale['sale_id']
                product_id = sale['product_id']
                quantity = int(sale['quantity'])
                price = float(sale['unit_price'])
                total = quantity * price

                grand_total += total
                total_quantity += quantity

                print(
                    f"{sale_id:<10}"
                    f"{product_id:<15}"
                    f"{quantity:>6}"
                    f"{price:>15,.2f}"
                    f"{total:>15,.2f}"
                )

            # สรุปยอดขาย
            print('-' * 65)
            print(f"{'Total items sold:':<30}{total_quantity:>35}")
            print(f"{'Total sales:':<30}{grand_total:>31,.2f} THB")
            print('=' * 65 + '\n')

        except FileNotFoundError:
            print('Sales file not found.')


