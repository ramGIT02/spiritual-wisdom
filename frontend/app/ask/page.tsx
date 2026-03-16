import AskForm from "./AskForm";

export default function AskPage() {
  return (
    <div style={{ display: "grid", gap: 20 }}>
      <div>
        <h1 style={{ marginBottom: 8 }}>Ask</h1>
        <p style={{ color: "#4b5563" }}>
          Ask a grounded spiritual question and receive a structured answer with sources.
        </p>
      </div>

      <AskForm />
    </div>
  );
}
