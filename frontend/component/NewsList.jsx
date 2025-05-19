import Link from "next/link";

export default function NewsList({ news }) {
  if (!news || news.length === 0) {
    return <div className="text-center text-gray-500 mt-10">Tidak ada berita.</div>;
  }

  return (
    <ul className="max-w-2xl mx-auto mt-10 space-y-8">
      {news.map((item) => (
        <li key={item.id} className="border-b pb-6">
          <Link href={`/news/${item.id}`}>
            <h3 className="text-xl font-semibold text-blue-700 hover:underline cursor-pointer">{item.judul}</h3>
          </Link>
          <div className="text-sm text-gray-500 mt-1">
            {item.tanggal} | {item.sumber}
          </div>
          {item.gambar_url && (
            <img src={item.gambar_url} alt={item.judul} className="max-w-xs mt-3 rounded" />
          )}
          <p className="mt-2 text-gray-700">
            {item.isi ? item.isi.substring(0, 120) + "..." : ""}
          </p>
        </li>
      ))}
    </ul>
  );
}