'use client';
import { useEffect, useState } from "react";
import Link from "next/link";

export default function NewsPage() {
  const [news, setNews] = useState([]);

  useEffect(() => {
    fetch('/data/all_news.json')
      .then(res => res.json())
      .then(setNews);
  }, []);

  return (
    <div className="flex items-center justify-center min-h-screen bg-gradient-to-br from-blue-200 via-purple-200 to-pink-200">
      <div className="backdrop-blur-md bg-white/40 rounded-xl shadow-lg p-10 max-w-3xl w-full border border-white/30">
        <h1 className="text-3xl font-bold mb-8 text-gray-900 drop-shadow text-center">Daftar Berita</h1>
        <ul className="space-y-8">
          {news.map(item => (
            <li key={item.id} className="bg-white/60 rounded-lg shadow p-6 hover:bg-white/80 transition border border-white/30">
              <Link href={`/news/${item.id}`}>
                <h3 className="text-xl font-semibold text-blue-700 hover:underline mb-2">{item.judul || "[Tanpa Judul]"}</h3>
              </Link>
              <div className="text-sm text-gray-600 mb-2">{item.tanggal} | {item.sumber}</div>
              {item.gambar_url && (
                <img
                  src={item.gambar_url}
                  alt={item.judul}
                  className="rounded-lg shadow mb-4 w-full max-h-52 object-cover"
                />
              )}
              <p className="text-gray-800">{item.isi ? item.isi.substring(0, 120) + "..." : ""}</p>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}