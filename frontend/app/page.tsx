import Link from "next/link";

type DailyWisdom = {
  reference: string;
  text: string;
  explanation: string;
  reflection_prompt: string;
};

type Source = {
  id: number;
  title: string;
  tradition: string;
  description: string;
};

type Concept = {
  id: number;
  name: string;
  short_definition: string;
};

type Practice = {
  id: number;
  name: string;
  tradition: string;
  duration_minutes: number;
  purpose: string;
};

async function getJson<T>(url: string): Promise<T> {
  const res = await fetch(url, { cache: "no-store" });
  if (!res.ok) throw new Error(`Failed to load ${url}`);
  return res.json();
}

export default async function HomePage() {
  const base = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";

  const [daily, sources, concepts, practices] = await Promise.all([
    getJson<DailyWisdom>(`${base}/daily-wisdom`),
    getJson<Source[]>(`${base}/sources`),
    getJson<Concept[]>(`${base}/concepts`),
    getJson<Practice[]>(`${base}/practices`),
  ]);

  return (
    <div style={{ display: "grid", gap: 24 }}>
      <section
        style={{
          background: "white",
          border: "1px solid #e5e7eb",
          borderRadius: 18,
          padding: 24,
        }}
      >
        <div style={{ fontSize: 14, color: "#6b7280" }}>Today&apos;s Wisdom</div>
        <h1 style={{ margin: "8px 0 4px", fontSize: 34 }}>Spiritual Wisdom Platform</h1>
        <p style={{ margin: 0, color: "#4b5563" }}>
          Explore scriptures, concepts, practices, and grounded spiritual guidance.
        </p>

        <div
          style={{
            marginTop: 20,
            border: "1px solid #e5e7eb",
            borderRadius: 16,
            padding: 20,
            background: "#f8fafc",
          }}
        >
          <div style={{ fontSize: 14, color: "#6b7280" }}>{daily.reference}</div>
          <div style={{ fontSize: 24, marginTop: 8, fontWeight: 600 }}>{daily.text}</div>
          <p style={{ marginTop: 14, color: "#374151" }}>{daily.explanation}</p>
          <p style={{ marginTop: 12, color: "#6b7280" }}>
            <strong>Reflect:</strong> {daily.reflection_prompt}
          </p>
        </div>
      </section>

      <section style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))", gap: 16 }}>
        <Link href="/scriptures" style={{ textDecoration: "none" }}>
          <div style={{ background: "white", border: "1px solid #e5e7eb", borderRadius: 16, padding: 18 }}>
            <h3 style={{ marginTop: 0 }}>Scriptures</h3>
            <p style={{ color: "#4b5563" }}>Browse source texts, chapters, and verses.</p>
          </div>
        </Link>

        <Link href="/concepts" style={{ textDecoration: "none" }}>
          <div style={{ background: "white", border: "1px solid #e5e7eb", borderRadius: 16, padding: 18 }}>
            <h3 style={{ marginTop: 0 }}>Concepts</h3>
            <p style={{ color: "#4b5563" }}>Explore Atman, Dharma, Nonduality, and more.</p>
          </div>
        </Link>

        <Link href="/practices" style={{ textDecoration: "none" }}>
          <div style={{ background: "white", border: "1px solid #e5e7eb", borderRadius: 16, padding: 18 }}>
            <h3 style={{ marginTop: 0 }}>Practices</h3>
            <p style={{ color: "#4b5563" }}>Learn meditation and spiritual practices.</p>
          </div>
        </Link>

        <Link href="/ask" style={{ textDecoration: "none" }}>
          <div style={{ background: "white", border: "1px solid #e5e7eb", borderRadius: 16, padding: 18 }}>
            <h3 style={{ marginTop: 0 }}>Ask</h3>
            <p style={{ color: "#4b5563" }}>Ask grounded spiritual questions.</p>
          </div>
        </Link>
      </section>

      <section style={{ display: "grid", gridTemplateColumns: "1.1fr 0.9fr", gap: 20 }}>
        <div style={{ background: "white", border: "1px solid #e5e7eb", borderRadius: 16, padding: 20 }}>
          <h2 style={{ marginTop: 0 }}>Featured Scriptures</h2>
          <div style={{ display: "grid", gap: 12 }}>
            {sources.slice(0, 5).map((source) => (
              <div key={source.id} style={{ border: "1px solid #e5e7eb", borderRadius: 12, padding: 14 }}>
                <div style={{ fontWeight: 600 }}>{source.title}</div>
                <div style={{ fontSize: 14, color: "#6b7280", marginTop: 4 }}>{source.tradition}</div>
                <div style={{ marginTop: 8, color: "#4b5563" }}>{source.description}</div>
              </div>
            ))}
          </div>
        </div>

        <div style={{ display: "grid", gap: 20 }}>
          <div style={{ background: "white", border: "1px solid #e5e7eb", borderRadius: 16, padding: 20 }}>
            <h2 style={{ marginTop: 0 }}>Featured Concepts</h2>
            <div style={{ display: "grid", gap: 10 }}>
              {concepts.slice(0, 5).map((concept) => (
                <div key={concept.id} style={{ border: "1px solid #e5e7eb", borderRadius: 12, padding: 12 }}>
                  <div style={{ fontWeight: 600 }}>{concept.name}</div>
                  <div style={{ marginTop: 6, color: "#4b5563" }}>{concept.short_definition}</div>
                </div>
              ))}
            </div>
          </div>

          <div style={{ background: "white", border: "1px solid #e5e7eb", borderRadius: 16, padding: 20 }}>
            <h2 style={{ marginTop: 0 }}>Featured Practices</h2>
            <div style={{ display: "grid", gap: 10 }}>
              {practices.slice(0, 4).map((practice) => (
                <div key={practice.id} style={{ border: "1px solid #e5e7eb", borderRadius: 12, padding: 12 }}>
                  <div style={{ fontWeight: 600 }}>{practice.name}</div>
                  <div style={{ fontSize: 14, color: "#6b7280", marginTop: 4 }}>
                    {practice.tradition} • {practice.duration_minutes} min
                  </div>
                  <div style={{ marginTop: 6, color: "#4b5563" }}>{practice.purpose}</div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}



