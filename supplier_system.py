import sqlite3

conn = sqlite3.connect("suppliers.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplier_name TEXT NOT NULL,
    product_name TEXT NOT NULL,
    price REAL NOT NULL,
    delivery_time TEXT NOT NULL,
    rating REAL,
    email TEXT,
    extra_feature TEXT
)
""")

conn.commit()

cursor.execute("""
SELECT * FROM suppliers
""")

suppliers = cursor.fetchall()

print("\n===== قائمة الموردين =====\n")

if len(suppliers) == 0:
    print("لا يوجد موردون حالياً.")
else:
    for supplier in suppliers:
        print(f"رقم المورد: {supplier[0]}")
        print(f"اسم المورد: {supplier[1]}")
        print(f"اسم المنتج: {supplier[2]}")
        print(f"السعر: {supplier[3]}")
        print(f"مدة التوصيل: {supplier[4]}")
        print(f"التقييم: {supplier[5]}")
        print(f"البريد الإلكتروني: {supplier[6]}")
        print(f"ميزة إضافية: {supplier[7]}")
        print("-" * 30)

conn.close()