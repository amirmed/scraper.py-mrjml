import requests

BASE = "https://payment.marjanemall.ma/media/amasty/elastic/import/"

found_images = []

# يمكن تعديل الرقم الأعلى حسب عدد الصور المتوقع
for i in range(1, 4201):  # يفحص 1.png إلى 200.png
    url = f"{BASE}{i}.png"
    try:
        r = requests.head(url, timeout=5)
        if r.status_code == 200:
            found_images.append(url)
            print("FOUND:", url)
    except:
        continue

# حفظ النتائج
with open("results.txt", "w", encoding="utf-8") as f:
    for img in found_images:
        f.write(img + "\n")

print("\nSaved results to results.txt")
