async function getDailyWisdom() {
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/daily-wisdom`, { cache: "no-store" });
  if (!res.ok) throw new Error("Failed to load daily wisdom");
  return res.json();
}

export default async function HomePage() {
  const daily = await getDailyWisdom();

  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: 32 }}>
      <h1>Spiritual Wisdom</h1>
      <div style={{ border: "1px solid #ddd", borderRadius: 16, padding: 24 }}>
        <div style={{ color: "#666", fontSize: 14 }}>{daily.reference}</div>
        <div style={{ fontSize: 24, marginTop: 8 }}>{daily.text}</div>
        <p style={{ marginTop: 16 }}>{daily.explanation}</p>
        <p style={{ marginTop: 16, color: "#666" }}>Reflect: {daily.reflection_prompt}</p>
      </div>
    </main>
  );
}
