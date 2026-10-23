from product_manager import Productmaneger
from file_manager import FileManager
from report_manager import report_sales_by_product

while True:
    num = input("1 = แสดงสินค้า, 2 = เมนู 2, 3 = เมนู 3, 4 = Exit, 5 = เพิ่มสินค้า: ")

    match num:
        case "1":
            print('1')
        case "2":
            print("2")

        case "3":
            print("3")

        case "4":
            print("Exit")
            break

        case "5":
            Productmaneger().show_product()

        case "6": 
            report_sales_by_product()

        case _:
            print("กรุณาเลือก 1-6")


