type Source = {
  id: number;
  title: string;
  tradition: string;
  description: string;
  chapters_count: number;
};

async function getSources(): Promise<Source[]> {
  const base = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";
  const res = await fetch(`${base}/sources`, { cache: "no-store" });
  if (!res.ok) throw new Error("Failed to load sources");
  return res.json();
}

export default async function ScripturesPage() {
  const sources = await getSources();

  return (
    <div style={{ display: "grid", gap: 20 }}>
      <div>
        <h1 style={{ marginBottom: 8 }}>Scriptures</h1>
        <p style={{ color: "#4b5563" }}>Browse the scripture sources available in the app.</p>
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))", gap: 16 }}>
        {sources.map((source) => (
          <div key={source.id} style={{ background: "white", border: "1px solid #e5e7eb", borderRadius: 16, padding: 18 }}>
            <h3 style={{ marginTop: 0 }}>{source.title}</h3>
            <div style={{ color: "#6b7280", fontSize: 14 }}>{source.tradition}</div>
            <p style={{ color: "#4b5563" }}>{source.description}</p>
            <div style={{ fontSize: 14, color: "#6b7280" }}>Chapters: {source.chapters_count}</div>
          </div>
        ))}
      </div>
    </div>
  );
}
