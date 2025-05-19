import requests
from bs4 import BeautifulSoup
import json
import uuid
import time
import random

BASE_URL = "https://www.liputan6.com"
LISTING_URL = f"{BASE_URL}/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; MyBot/1.0; +https://example.com/bot-info)"
}

def ambil_daftar_berita(max_berita=3):
    try:
        r = requests.get(LISTING_URL, headers=HEADERS, timeout=10)
        r.raise_for_status()
    except Exception as e:
        print(f"❌ Gagal mengambil daftar berita: {e}")
        return []

    soup = BeautifulSoup(r.text, "lxml")
    hasil = []
    seen_links = set()  # Track links we've already processed

    # Fix: Use correct selector for article items
    items = soup.select("article")

    if not items:
        print("⚠️ Tidak ditemukan berita di halaman listing.")
        return []

    count = 0
    for item in items:
        if count >= max_berita:
            break

        # Fix: Use correct selectors for title and link
        title_tag = item.select_one("span.articles--iridescent-list--text-item__title-link-text")
        link_tag = item.select_one("h4 a")

        if title_tag and link_tag and link_tag.has_attr("href"):
            title = title_tag.text.strip()
            link = link_tag["href"]

            # Ensure link is absolute
            if not link.startswith(("http://", "https://")):
                link = BASE_URL + link

            # Skip if we've already seen this link
            if link in seen_links:
                print(f"⚠️ Melewati artikel duplikat: {title[:30]}...")
                continue

            seen_links.add(link)

            hasil.append({
                "judul": title[:100],
                "link": link
            })
            count += 1
            print(f"✅ Artikel #{count}: {title[:50]}...")
        else:
            print("⚠️ Berita tidak memiliki judul atau link, dilewati.")

    print(f"📊 Total artikel unik yang ditemukan: {len(hasil)}")
    return hasil

def ambil_detail(link):
    try:
        r = requests.get(link, headers=HEADERS, timeout=10)
        r.raise_for_status()
    except Exception as e:
        raise Exception(f"Gagal mengambil detail: {e}")

    soup = BeautifulSoup(r.text, "lxml")

    # Fix: Use proper selector for date
    tanggal_tag = soup.select_one("span.read-page-box__author__updated")
    tanggal = tanggal_tag.get_text(strip=True) if tanggal_tag else "Tanggal tidak ditemukan"

    # Fix: Use proper selector for content
    konten = soup.select_one("div.article-content-body__item-page")
    if not konten:
        raise Exception("Konten berita tidak ditemukan")

    paragraf = konten.select("p")
    isi = "\n".join([p.get_text(strip=True) for p in paragraf]) if paragraf else "Isi tidak tersedia"

    # Fix: Use proper selector for image
    gambar_tag = soup.select_one("picture img")
    gambar_url = gambar_tag["src"] if gambar_tag and gambar_tag.has_attr("src") else ""

    return {
        "tanggal": tanggal,
        "isi": isi,
        "gambar_url": gambar_url
    }

def scrape_liputan6_detail(max_berita=3):
    daftar = ambil_daftar_berita(max_berita)
    if not daftar:
        print("❌ Tidak ada berita yang bisa diambil.")
        return []

    hasil = []
    for berita in daftar:
        print(f"🔍 {berita['judul']}")
        try:
            detail = ambil_detail(berita["link"])
            hasil.append({
                "id": str(uuid.uuid4()),
                "judul": berita["judul"],
                "tanggal": detail["tanggal"],
                "isi": detail["isi"],
                "gambar_url": detail["gambar_url"],
                "sumber": "Liputan6"
            })
            print("   ✅ Berhasil")
        except Exception as e:
            print(f"   ❌ Gagal: {e}")
        time.sleep(random.uniform(1, 2))
    return hasil

def simpan_ke_json(data, filename="berita_liputan6.json"):
    if not data:
        print("⚠️ Tidak ada data untuk disimpan.")
        return
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"\n✅ Data disimpan ke {filename}")
    except Exception as e:
        print(f"❌ Gagal menyimpan file JSON: {e}")

# Fix: Correct the main block syntax
if __name__ == "__main__":
    hasil = scrape_liputan6_detail()
    simpan_ke_json(hasil)
