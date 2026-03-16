"use client";

import { useState } from "react";
import { apiPost } from "@/lib/api";

type AskResponse = {
  answer: string;
  sources: string[];
  related_concepts: string[];
  suggested_practice?: string | null;
  disclaimer: string;
};

export default function AskForm() {
  const [question, setQuestion] = useState("What is Atman?");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<AskResponse | null>(null);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await apiPost<AskResponse>("/ask", {
        question,
        mode: "simple",
      });
      setResult(response);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Unknown error");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{ background: "white", border: "1px solid #e5e7eb", borderRadius: 16, padding: 20 }}>
      <form onSubmit={handleSubmit} style={{ display: "grid", gap: 14 }}>
        <label style={{ display: "grid", gap: 8 }}>
          <span style={{ fontWeight: 600 }}>Ask a spiritual question</span>
          <textarea
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            rows={5}
            style={{ width: "100%", padding: 12, borderRadius: 12, border: "1px solid #d1d5db" }}
            placeholder="What is Atman?"
          />
        </label>

        <button
          type="submit"
          disabled={loading}
          style={{
            width: 160,
            padding: "12px 16px",
            borderRadius: 12,
            border: "none",
            background: "#111827",
            color: "white",
            cursor: "pointer",
          }}
        >
          {loading ? "Asking..." : "Ask"}
        </button>
      </form>

      {error && (
        <div style={{ marginTop: 18, color: "#b91c1c" }}>
          <strong>Error:</strong> {error}
        </div>
      )}

      {result && (
        <div style={{ marginTop: 22, display: "grid", gap: 16 }}>
          <div>
            <h3 style={{ marginBottom: 8 }}>Answer</h3>
            <div style={{ color: "#374151", whiteSpace: "pre-wrap" }}>{result.answer}</div>
          </div>

          <div>
            <h3 style={{ marginBottom: 8 }}>Sources</h3>
            <ul>
              {result.sources.map((source) => (
                <li key={source}>{source}</li>
              ))}
            </ul>
          </div>

          <div>
            <h3 style={{ marginBottom: 8 }}>Related Concepts</h3>
            <ul>
              {result.related_concepts.map((concept) => (
                <li key={concept}>{concept}</li>
              ))}
            </ul>
          </div>

          {result.suggested_practice && (
            <div>
              <h3 style={{ marginBottom: 8 }}>Suggested Practice</h3>
              <div>{result.suggested_practice}</div>
            </div>
          )}

          <div style={{ color: "#6b7280", fontSize: 14 }}>{result.disclaimer}</div>
        </div>
      )}
    </div>
  );
}

