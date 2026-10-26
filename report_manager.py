
def report_sales_by_product():
    products = {}

    # Read product data
    try:
        with open('products.csv', 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines[1:]:
                parts = line.strip().split(',')

                if len(parts) < 4:
                    continue

                product_id = parts[0].strip()
                product_name = parts[1].strip()
                price = float(parts[2])
                stock = int(parts[3])

                products[product_id] = {
                    'name': product_name,
                    'price': price,
                    'stock': stock,
                    'sold_qty': 0,
                    'total_sales': 0.0
                }

    except FileNotFoundError:
        print('Error: products.txt not found.')
        return
    except ValueError:
        print('Error: Invalid product data.')
        return

    # Read sales data
    try:
        with open('sales.csv', 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines[1:]:
                parts = line.strip().split(',')

                if len(parts) < 5:
                    continue

                product_id = parts[1].strip()
                quantity = int(parts[2])
                unit_price = float(parts[3])

                if product_id in products:
                    products[product_id]['sold_qty'] += quantity
                    products[product_id]['total_sales'] += (
                        quantity * unit_price
                    )

    except FileNotFoundError:
        print('Error: sales.txt not found.')
        return
    except ValueError:
        print('Error: Invalid sales data.')
        return

    # Display report
    print('\n' + '=' * 75)
    print(
        f"{'Product':<20}"
        f"{'Sold Qty':>12}"
        f"{'Total Sales':>18}"
        f"{'Stock':>12}"
    )
    print('=' * 75)

    for product_id, data in products.items():
        print(
            f"{data['name']:<20}"
            f"{data['sold_qty']:>12,d}"
            f"{data['total_sales']:>15,.2f} THB"
            f"{data['stock']:>9,d}"
        )

    print('=' * 75 + '\n')



