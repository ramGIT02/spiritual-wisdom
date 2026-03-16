type Practice = {
  id: number;
  name: string;
  tradition: string;
  duration_minutes: number;
  purpose: string;
  benefits: string;
  common_mistakes: string;
};

async function getPractices(): Promise<Practice[]> {
  const base = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";
  const res = await fetch(`${base}/practices`, { cache: "no-store" });
  if (!res.ok) throw new Error("Failed to load practices");
  return res.json();
}

export default async function PracticesPage() {
  const practices = await getPractices();

  return (
    <div style={{ display: "grid", gap: 20 }}>
      <div>
        <h1 style={{ marginBottom: 8 }}>Practices</h1>
        <p style={{ color: "#4b5563" }}>Meditation and spiritual practices you can explore.</p>
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))", gap: 16 }}>
        {practices.map((practice) => (
          <div key={practice.id} style={{ background: "white", border: "1px solid #e5e7eb", borderRadius: 16, padding: 18 }}>
            <h3 style={{ marginTop: 0 }}>{practice.name}</h3>
            <div style={{ color: "#6b7280", fontSize: 14 }}>
              {practice.tradition} • {practice.duration_minutes} min
            </div>
            <p style={{ color: "#374151", marginTop: 10 }}><strong>Purpose:</strong> {practice.purpose}</p>
            <p style={{ color: "#4b5563" }}><strong>Benefits:</strong> {practice.benefits}</p>
            <p style={{ color: "#4b5563" }}><strong>Common mistakes:</strong> {practice.common_mistakes}</p>
          </div>
        ))}
      </div>
    </div>
  );
}



