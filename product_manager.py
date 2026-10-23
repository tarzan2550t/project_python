import os
from datetime import date

def load_products():
    """อ่านสินค้าทั้งหมดจาก products.txt"""
    products = []
    if not os.path.exists(PRODUCT_FILE):
        return products
    with open(PRODUCT_FILE, "r", encoding="utf-8") as f:
        for line in f.read().splitlines()[1:]:  # ข้ามบรรทัดหัวตาราง
            if line.strip():
                products.append(Product.from_line(line))
    return products


def save_products(products):
    """เขียนสินค้าทั้งหมดลง products.txt"""
    with open(PRODUCT_FILE, "w", encoding="utf-8") as f:
        f.write(HEADER + "\n")
        for p in products:
            f.write(p.to_line() + "\n")


def add_product(name, price, stock):
    """เพิ่มสินค้าใหม่ (รหัสรันอัตโนมัติ, วันที่ = วันนี้) คืนค่า Product ที่เพิ่ม"""
    name = name.strip()
    if not name or "," in name:
        raise ValueError("ชื่อสินค้าต้องไม่ว่าง และห้ามมีเครื่องหมาย ,")
    if price < 0 or stock < 0:
        raise ValueError("ราคาและจำนวนต้องไม่ติดลบ")

    products = load_products()
    new_id = max((p.id for p in products), default=0) + 1
    product = Product(new_id, name, price, stock, date.today().isoformat())
    products.append(product)
    save_products(products)
    return product

def list_products():
    """แสดงรายการสินค้าทั้งหมด"""
    products = load_products()
    if not products:
        print("ยังไม่มีสินค้าในระบบ")
        return
    for p in products:
        print(f"[{p.id}] {p.name} - {p.price:,.2f} บาท (คงเหลือ {p.stock})")


def product_report():
    """รายงานข้อมูลสินค้า: รหัส ชื่อ ราคา คงเหลือ วันที่เพิ่ม"""
    products = load_products()
    line = "=" * 68
    print(line)
    print("รายงานข้อมูลสินค้า".center(68))
    print(line)
    print(f"{'รหัส':<6}{'ชื่อสินค้า':<24}{'ราคา':>12}{'คงเหลือ':>10}{'วันที่เพิ่ม':>14}")
    print("-" * 68)
    for p in products:
        print(f"{p.id:<6}{p.name:<24}{p.price:>12,.2f}{p.stock:>10}{p.date:>14}")
        print("-" * 68)
        print(f"รวมทั้งหมด {len(products)} รายการ")