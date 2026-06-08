import sqlite3
import csv

# 1. الاتصال بقاعدة البيانات
conn = sqlite3.connect("suppliers.db")
cursor = conn.cursor()

# حذف الجدول القديم لإعادة بنائه بالهيكلية المطلوبة بالضبط
cursor.execute("DROP TABLE IF EXISTS suppliers")

# إنشاء الجدول بالأعمدة الـ 8 الأساسية التي طلبتيها فقط
cursor.execute("""
CREATE TABLE IF NOT EXISTS suppliers (
    product_name TEXT NOT NULL,
    supplier_name TEXT NOT NULL,
    price REAL NOT NULL,
    delivery_days INTEGER NOT NULL,
    rating REAL,
    stock_quantity INTEGER,
    min_order INTEGER,
    email TEXT
)
""")
conn.commit()

# 2. البيانات الـ 33 كاملة بنفس أسمائها المخصصة والدقيقة وبدون أي تغيير
suppliers_data = [
    ("Laptop HP", "شركة الاتصالات", 2500, 3, 4.5, 850, 10, "info@generalcomms.com"),
    ("Monitor Samsung", "شركة التقنية للجميع", 1500, 5, 4.8, 1200, 5, "support@tech4all.com"),
    ("Printer Dell", "مؤسسة تقني روعة", 500, 7, 3.5, 340, 2, "contact@taqniroaa.com"),
    ("Luxury Desk Organizer", "شركة كماليات جنان", 450, 2, 4.2, 95, 20, "sales@jananluxury.com"),
    ("Ergonomic Office Chair", "مؤسسة تجهيزاتك هنا", 400, 5, 4.5, 620, 10, "orders@kathaequip.com"),
    ("Golden Fountain Pen", "شركة مكتبك الذهبي", 300, 3, 4.9, 180, 5, "info@goldenlibrary.com"),
    ("Premium Olive Oil", "توردات الخليجية", 1200, 5, 4.7, 1450, 50, "sales@gulfsupplies.com"),
    ("Organic Honey Box", "شركة غذاء الجميع", 600, 7, 4.3, 780, 30, "contact@foodforall.com"),
    ("Basmati Rice 10kg", "مؤسسة منتجات", 300, 9, 4.0, 260, 10, "info@montajat.com"),
    ("Mechanical Keyboard", "شركة التقنية الحديثة", 3800, 4, 4.8, 980, 5, "support@modemtech.com"),
    ("Wireless Gaming Mouse", "توريدات الأمل للتقنية", 2000, 7, 4.5, 430, 10, "sales@amaltech.com"),
    ("Anker Power Bank", "مؤسسة سعد للأجهزة", 1500, 14, 4.2, 150, 3, "orders@saaddevices.com"),
    ("Classic Wooden Desk", "مؤسسة الرؤية", 5200, 7, 4.1, 710, 1, "info@alruya.com"),
    ("Leather Sofa Set", "مؤسسة السلام", 7000, 5, 4.2, 290, 5, "contact@alsalam.com"),
    ("Meeting Room Table", "شركة أقلام", 3000, 3, 4.5, 1750, 2, "sales@aqlam.com"),
    ("4K IP Camera Hikvision", "مؤسسة الإبداع", 1800, 3, 4.6, 520, 3, "info@techcreativity.com"),
    ("Smart Door Lock", "مؤسسة الرقابة", 1000, 9, 4.1, 85, 5, "support@raqaba.com"),
    ("8CH NVR Recorder", "شركة راقب للكاميرات", 750, 7, 4.7, 310, 1, "sales@raqibcams.com"),
    ("Silk Fabric Roll", "شركة توريدات الهلال", 900, 6, 4.0, 1340, 30, "orders@hilalsupply.com"),
    ("Custom Men Thobe", "مؤسسة خياط السعد", 600, 3, 4.6, 120, 15, "contact@saadtailor.com"),
    ("Winter Wool Jacket", "شركة حياكة للملابس", 300, 7, 4.9, 680, 10, "sales@hekayaiafashion.com"),
    ("Industrial Detergent", "شركة الإتقان", 300, 1, 4.4, 410, 15, "info@aletqan.com"),
    ("Vacuum Cleaner Pro", "مؤسسة كلين", 1500, 5, 4.6, 230, 10, "support@cleanco.com"),
    ("Microfiber Towels Pack", "شركة بريق", 450, 7, 4.0, 560, 5, "contact@bareeq.com"),
    ("Organic Fertilizer Bag", "مؤسسة الراحة الآمنة", 1500, 3, 4.3, 140, 10, "info@safecomfort.com"),
    ("Automatic Water Pump", "شركة الطبيعة", 1000, 9, 4.5, 890, 5, "contact@naturalco.com"),
    ("Greenhouse Seeds Kit", "توريدات الخضراء", 750, 5, 4.8, 370, 15, "sales@greensupply.com"),
    ("Brembo Brake Pads", "شركة التوفير لسيارات", 2200, 2, 4.7, 75, 5, "info@savingcars.com"),
    ("Mobil Engine Oil 1L", "توريدات الأوفر", 1000, 5, 4.2, 1120, 10, "orders@alwafeer.com"),
    ("LED Headlight Bulb", "مؤسسة الحجاز", 1300, 9, 4.9, 460, 15, "contact@alhijaz.com"),
    ("Oak Wood Planks", "شركة الخشب الأصيل", 700, 8, 4.3, 205, 6, "sales@originalwood.com"),
    ("MDF Fiberboard Sheet", "مؤسسة خشيبك الأتقن", 450, 5, 4.8, 640, 3, "info@khashabak.com"),
    ("Plywood Waterproof", "توريدات أخشاب فهد", 600, 3, 4.5, 920, 9, "orders@fahdwood.com")
]

# إدخال البيانات في قاعدة البيانات
cursor.executemany("""
INSERT INTO suppliers (product_name, supplier_name, price, delivery_days, rating, stock_quantity, min_order, email)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", suppliers_data)
conn.commit()

# 3. جلب البيانات للتأكد وعرضها في الترمينال بالترتيب المطلوب
cursor.execute("SELECT * FROM suppliers")
suppliers = cursor.fetchall()

print("\n===== استعراض البيانات المنسقة بالترتيب المطلوب بالضبط =====\n")
for s in suppliers:
    print(f"Product: {s[0]:<23} | Supplier: {s[1]:<15} | Price: {s[2]:<6} | Days: {s[3]:<3} | Rating: {s[4]:<4} | Stock: {s[5]:<5} | Min: {s[6]:<3} | Email: {s[7]}")
    print("-" * 120)

# 4. تصدير البيانات إلى ملف الأكسل (CSV) بالأعمدة الـ 8 المحددة فقط وبترتيبكِ الخاص
with open("suppliers_excel.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    
    # أسماء الأعمدة الـ 8 المطلوبة بالضبط بالإنجليزية
    writer.writerow([
        "Product Name", "Supplier Name", "Price", "Delivery Days", 
        "Rating", "Stock Quantity", "Min Order", "Email"
    ])
    
    writer.writerows(suppliers)

print("\n[تم تحديث ملف الأكسل وقاعدة البيانات بالترتيب المعتمد والأسماء الـ 8 المطلوبة فقط!]\n")
conn.close()