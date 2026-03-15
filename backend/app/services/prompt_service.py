from typing import Sequence


def build_ask_prompt(question: str, mode: str, retrieved_chunks: Sequence[dict]) -> str:
    sources_block = "\n\n".join(
        [
            f"Source: {item['source_label']}\nTitle: {item.get('title') or ''}\nContent: {item['content']}"
            for item in retrieved_chunks
        ]
    )

    return f"""
You are a careful spiritual literature guide.
Answer ONLY using the retrieved material below.
Do not invent scripture references.
Do not claim certainty where traditions differ.
Clearly distinguish direct teaching from interpretation.

User question:
{question}

Response mode:
{mode}

Retrieved material:
{sources_block}

Return a structured answer with:
1. Direct answer
2. Relevant sources
3. Practical meaning
4. Suggested next step or meditation when appropriate
""".strip()
