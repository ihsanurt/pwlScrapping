import requests
from bs4 import BeautifulSoup
import json
import uuid
import time
import random

BASE_URL = "https://www.tempo.co"
LISTING_URL = f"{BASE_URL}/indeks"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def ambil_daftar_berita(max_berita=3):
    r = requests.get(LISTING_URL, headers=HEADERS)
    soup = BeautifulSoup(r.text, "lxml")
    hasil = []
    for item in soup.select("div.flex.flex-col.divide-y.divide-neutral-500 figure")[:max_berita]:
        a_tag = item.select("a")
        if not a_tag:
            continue

        title = a_tag[1].text.strip()
        link = a_tag[1]["href"]
        hasil.append({
            "judul": title[:100],
            "link": link
        })
    return hasil

def ambil_detail(link):
    r = requests.get(link, headers=HEADERS)
    soup = BeautifulSoup(r.text, "lxml")
    tanggal_tag = soup.select_one("p.text-neutral-900.text-sm")
    tanggal = tanggal_tag.get_text(strip=True) if tanggal_tag else ""
    konten = soup.select_one("div#content-wrapper")
    paragraf = konten.find_all("p") if konten else []
    isi = "\n".join([p.get_text(strip=True) for p in paragraf])
    gambar_tag = soup.find("figure")
    img = gambar_tag.find("img") if gambar_tag else None
    gambar_url = img["src"] if img and img.has_attr("src") else ""
    return {
        "tanggal": tanggal,
        "isi": isi,
        "gambar_url": gambar_url
    }

def scrape_tempo_detail(max_berita=3):
    daftar = ambil_daftar_berita(max_berita)
    hasil = []
    for berita in daftar:
        print(f"🔍 {berita['judul']}")
        try:
            detail = ambil_detail(BASE_URL + berita["link"])
            hasil.append({
                "id": str(uuid.uuid4()),
                "judul": berita["judul"],
                "tanggal": detail["tanggal"],
                "isi": detail["isi"],
                "gambar_url": detail["gambar_url"],
                "sumber": "Tempo.co"
            })
            print("   ✅ Berhasil")
        except Exception as e:
            print(f"   ❌ Gagal: {e}")
        time.sleep(random.uniform(1, 2))
    return hasil

def simpan_ke_json(data, filename="berita_tempo.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Data disimpan ke {filename}")

if __name__ == "__main__":
    hasil = scrape_tempo_detail()
    simpan_ke_json(hasil)