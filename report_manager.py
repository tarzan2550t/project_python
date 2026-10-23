def report_sales_by_product():
    products = {}

    
    try:
        with open('products.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:  # อ่านทุกบรรทัดเพราะในไฟล์ไม่มี Header
                parts = line.strip().split(',')
                if len(parts) >= 4:
                    p_id = parts[0].strip()
                    name = parts[1].strip()
                    stock = int(parts[3])
                    
                    products[p_id] = {
                        'name': name,
                        'stock': stock,
                        'sold_qty': 0,
                        'total_sales': 0.0
                    }
    except FileNotFoundError:
        print("❌ ไม่พบไฟล์ products.txt")
        return

    
    try:
        with open('sales.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines[1:]:  # ข้าม Header ของไฟล์ sales.txt
                parts = line.strip().split(',')
                if len(parts) >= 5:
                    p_id = parts[1].strip()
                    quantity = int(parts[2])
                    unit_price = float(parts[3])
                    
                    if p_id in products:
                        products[p_id]['sold_qty'] += quantity
                        products[p_id]['total_sales'] += quantity * unit_price
    except FileNotFoundError:
        print("❌ ไม่พบไฟล์ sales.txt")
        return

    
    print("\n" + "=" * 62)
    print(f"{'สินค้า':^18}  {'ขายได้ทั้งหมด':^15}  {'ยอดขายรวม':^15}  {'คงเหลือ':^10}")
    print("=" * 62)
    
    for p_id, data in products.items():
        name = data['name']
        sold_qty = data['sold_qty']
        total_sales = data['total_sales']
        stock = data['stock']
        
        sales_str = f"{int(total_sales):,} บาท"
        
        print(f"{name:<18}   {sold_qty:^10,d}   {sales_str:^12}   {stock:^10,d}")
        
    print("=" * 62 + "\n")

# สำหรับทดสอบรันไฟล์นี้ไฟล์เดียว
if __name__ == "__main__":
    report_sales_by_product()
