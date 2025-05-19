import Link from "next/link";

export default function NewsDetail({ news }) {
  if (!news) return (
    <div className="flex items-center justify-center min-h-screen bg-gradient-to-br from-blue-200 via-purple-200 to-pink-200">
      <div className="backdrop-blur-md bg-white/40 rounded-xl shadow-lg p-8 border border-white/30">
        <span className="text-lg font-semibold text-gray-700">Loading...</span>
      </div>
    </div>
  );

  return (
    <div className="flex items-center justify-center min-h-screen bg-gradient-to-br from-blue-200 via-purple-200 to-pink-200">
      <div className="backdrop-blur-md bg-white/40 rounded-xl shadow-lg p-8 max-w-2xl w-full border border-white/30">
        <h1 className="text-3xl font-bold mb-2 text-gray-900 drop-shadow">{news.judul}</h1>
        <div className="text-sm text-gray-600 mb-4">{news.tanggal} | {news.sumber}</div>
        {news.gambar_url && (
          <img
            src={news.gambar_url}
            alt={news.judul}
            className="rounded-lg shadow mb-6 w-full max-h-80 object-cover"
          />
        )}
        <div className="text-gray-800 whitespace-pre-line mb-8" style={{lineHeight: "1.7"}}>
          {news.isi}
        </div>
        <Link
          href="/news"
          className="inline-block px-6 py-2 bg-white/60 hover:bg-white/80 text-blue-700 font-semibold rounded-lg shadow transition backdrop-blur border border-white/30"
        >
          ← Kembali ke daftar berita
        </Link>
      </div>
    </div>
  );
}