
from product_manager import Productmaneger
from report_manager import report_sales_by_product
from sales_manager import SalesManager

while True:
    print("=" * 40)
    print(f"{'MAIN MENU':^40}")
    print("=" * 40)
    print(f"| {'1. Add Product':<37}|")
    print(f"| {'2. Show Product':<37}|")
    print(f"| {'3. Record Sale':<37}|")
    print(f"| {'4. Show Sales':<37}|")
    print(f"| {'5. Report Daily Sales':<37}|")
    print(f"| {'6. Report Sales by Product':<37}|")
    print(f"| {'0. Exit Program':<37}|")
    print("=" * 40)

    num = input("Select choice: ")

    match num:
        case "1":
            Productmaneger().add_product()

        case "2":
            Productmaneger().show_product()

        case "3":
            SalesManager().add_sale()

        case "4":
            print("Show Sales")

        case "5":
            print("Report Daily Sales")

        case "6":
            report_sales_by_product()

        case "0":
            print("Exit Program....")
            break

        case _:
            print("Please select 0-6")
