
type Concept = {
  id: number;
  name: string;
  short_definition: string;
  detailed_explanation: string;
};

async function getConcepts(): Promise<Concept[]> {
  const base = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";
  const res = await fetch(`${base}/concepts`, { cache: "no-store" });
  if (!res.ok) throw new Error("Failed to load concepts");
  return res.json();
}

export default async function ConceptsPage() {
  const concepts = await getConcepts();

  return (
    <div style={{ display: "grid", gap: 20 }}>
      <div>
        <h1 style={{ marginBottom: 8 }}>Concepts</h1>
        <p style={{ color: "#4b5563" }}>Explore key spiritual and philosophical concepts.</p>
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))", gap: 16 }}>
        {concepts.map((concept) => (
          <div key={concept.id} style={{ background: "white", border: "1px solid #e5e7eb", borderRadius: 16, padding: 18 }}>
            <h3 style={{ marginTop: 0 }}>{concept.name}</h3>
            <p style={{ color: "#374151", fontWeight: 500 }}>{concept.short_definition}</p>
            <p style={{ color: "#4b5563" }}>{concept.detailed_explanation}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

