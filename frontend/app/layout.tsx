
import "./globals.css";
import Link from "next/link";
import type { ReactNode } from "react";

export const metadata = {
  title: "Spiritual Wisdom",
  description: "Scriptures, concepts, practices, and grounded spiritual guidance",
};

function NavLink({ href, children }: { href: string; children: ReactNode }) {
  return (
    <Link
      href={href}
      style={{
        padding: "10px 14px",
        borderRadius: 10,
        textDecoration: "none",
        color: "#1f2937",
        fontWeight: 500,
      }}
    >
      {children}
    </Link>
  );
}

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body style={{ margin: 0, fontFamily: "Arial, sans-serif", background: "#f8fafc", color: "#111827" }}>
        <header
          style={{
            borderBottom: "1px solid #e5e7eb",
            background: "white",
            position: "sticky",
            top: 0,
            zIndex: 20,
          }}
        >
          <div
            style={{
              maxWidth: 1100,
              margin: "0 auto",
              padding: "16px 20px",
              display: "flex",
              alignItems: "center",
              justifyContent: "space-between",
              gap: 16,
            }}
          >
            <Link href="/" style={{ textDecoration: "none", color: "#111827", fontSize: 22, fontWeight: 700 }}>
              Spiritual Wisdom
            </Link>

            <nav style={{ display: "flex", flexWrap: "wrap", gap: 6 }}>
              <NavLink href="/">Home</NavLink>
              <NavLink href="/scriptures">Scriptures</NavLink>
              <NavLink href="/concepts">Concepts</NavLink>
              <NavLink href="/practices">Practices</NavLink>
              <NavLink href="/ask">Ask</NavLink>
            </nav>
          </div>
        </header>

        <main style={{ maxWidth: 1100, margin: "0 auto", padding: 24 }}>{children}</main>
      </body>
    </html>
  );
}