import requests
from bs4 import BeautifulSoup
import json
import uuid
import time
import random

BASE_URL = "https://www.antaranews.com"
LISTING_URL = f"{BASE_URL}/terkini"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; MyBot/1.0; +https://example.com/bot-info)"
}

def ambil_daftar_berita(max_berita=3):
    r = requests.get(LISTING_URL, headers=HEADERS)
    soup = BeautifulSoup(r.text, "lxml")
    hasil = []
    for item in soup.select("div.wrapper__list__article div.card__post")[:max_berita]:
        a_tag = item.find("a")
        if not a_tag:
            continue
        title = a_tag.text.strip()
        link = a_tag["href"]
        if not link.startswith("http"):
            link = BASE_URL + link
        hasil.append({
            "judul": title[:100],
            "link": link
        })
    return hasil

def ambil_detail(link):
    r = requests.get(link, headers=HEADERS)
    soup = BeautifulSoup(r.text, "lxml")
    tanggal_tag = soup.select_one("div.wrap__article-detail-info span")
    tanggal = tanggal_tag.get_text(strip=True) if tanggal_tag else ""
    konten = soup.select_one("div.post-content")
    paragraf = konten.select("p") if konten else []
    isi = "\n".join([p.get_text(strip=True) for p in paragraf])
    gambar_tag = soup.select_one("div.wrap__article-detail-image img")
    gambar_url = gambar_tag["src"] if gambar_tag and gambar_tag.has_attr("src") else ""
    if gambar_url and not gambar_url.startswith("http"):
        gambar_url = BASE_URL + gambar_url
    return {
        "tanggal": tanggal,
        "isi": isi,
        "gambar_url": gambar_url
    }

def scrape_antara_detail(max_berita=3):
    daftar = ambil_daftar_berita(max_berita)
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
                "sumber": "Antara News"
            })
            print("   ✅ Berhasil")
        except Exception as e:
            print(f"   ❌ Gagal: {e}")
        time.sleep(random.uniform(1, 2))
    return hasil

def simpan_ke_json(data, filename="berita_antara.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Data disimpan ke {filename}")

if __name__ == "__main__":
    hasil = scrape_antara_detail()
    simpan_ke_json(hasil)
