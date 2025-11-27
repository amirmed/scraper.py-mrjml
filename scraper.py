import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

BASE_URL = "https://marjanemall.ma"
FILTER_PATH = "/media/amasty/elastic/import"

visited = set()
to_visit = [BASE_URL]

found_images = []

def is_valid(url):
    return urlparse(url).netloc == urlparse(BASE_URL).netloc

while to_visit:
    url = to_visit.pop()
    if url in visited:
        continue

    visited.add(url)

    try:
        print("Scanning:", url)
        resp = requests.get(url, timeout=5)
        html = resp.text
    except:
        continue

    soup = BeautifulSoup(html, "html.parser")

    # جمع الروابط
    for link in soup.find_all("a", href=True):
        new_url = urljoin(url, link["href"])
        if is_valid(new_url) and new_url not in visited:
            to_visit.append(new_url)

    # جمع الصور
    for img in soup.find_all("img", src=True):
        img_url = urljoin(url, img["src"])
        if FILTER_PATH in img_url:
            found_images.append(img_url)
            print("FOUND:", img_url)

# حفظ النتائج
with open("results.txt", "w", encoding="utf-8") as f:
    for img in found_images:
        f.write(img + "\n")

print("\nSaved results to results.txt")
