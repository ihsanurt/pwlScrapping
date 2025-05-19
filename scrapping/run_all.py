# run_all.py
import json
from antara import scrape_antara_detail
from tempo import scrape_tempo_detail
from liputan6 import scrape_liputan6_detail

def run():
    all_news = scrape_antara_detail() + scrape_tempo_detail() + scrape_liputan6_detail()

    with open("data/all_news.json", "w", encoding="utf-8") as f:
        json.dump(all_news, f, ensure_ascii=False, indent=2)

    print("✅ Data berhasil disimpan ke data/all_news.json")

if __name__ == "__main__":
    run()