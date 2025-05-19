export default function Home() {
  return (
    <div className="flex items-center justify-center min-h-screen bg-gradient-to-br from-blue-200 via-purple-200 to-pink-200">
      <div className="backdrop-blur-md bg-white/40 rounded-xl shadow-lg p-10 max-w-lg w-full text-center border border-white/30">
        <h1 className="text-4xl font-bold mb-6 text-gray-900 drop-shadow">Portal Berita</h1>
        <a
          href="/login"
          className="inline-block px-8 py-3 bg-white/60 hover:bg-white/80 text-blue-700 font-semibold rounded-lg shadow transition backdrop-blur border border-white/30"
        >
          Login dengan Google untuk melihat berita
        </a>
      </div>
    </div>
  );
}