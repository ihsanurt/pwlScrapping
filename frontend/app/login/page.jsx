'use client';
import { signIn, useSession } from 'next-auth/react';

export default function LoginPage() {
  const { data: session } = useSession();

  if (session) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-gradient-to-br from-blue-200 via-purple-200 to-pink-200">
        <div className="backdrop-blur-md bg-white/40 rounded-xl shadow-lg p-10 max-w-lg w-full text-center border border-white/30">
          <p className="mb-4 text-lg text-gray-800">
            Sudah login sebagai <span className="font-semibold">{session.user.email}</span>
          </p>
          <a
            href="/news"
            className="inline-block px-8 py-3 bg-white/60 hover:bg-white/80 text-blue-700 font-semibold rounded-lg shadow transition backdrop-blur border border-white/30"
          >
            Lihat Berita
          </a>
        </div>
      </div>
    );
  }

  return (
    <div className="flex items-center justify-center min-h-screen bg-gradient-to-br from-blue-200 via-purple-200 to-pink-200">
      <div className="backdrop-blur-md bg-white/40 rounded-xl shadow-lg p-10 max-w-lg w-full text-center border border-white/30">
        <h2 className="text-2xl font-bold mb-6 text-gray-900 drop-shadow">Login dengan Google</h2>
        <button
          onClick={() => signIn('google')}
          className="px-8 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition font-semibold shadow"
        >
          Login Google
        </button>
      </div>
    </div>
  );
}