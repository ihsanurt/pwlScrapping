export async function getAllNews() {
  const res = await fetch('/api/news');
  return res.json();
}

export async function getNewsById(id) {
  const res = await fetch('/api/news');
  const news = await res.json();
  return news.find(item => item.id === id);
}