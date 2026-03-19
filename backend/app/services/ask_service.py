from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.ask_log import AskLog
from app.schemas.ask import AskRequest, AskResponse
from app.services.llm_client import client
from app.services.prompt_service import build_ask_prompt
from app.services.retrieval_service import retrieve_chunks


def answer_question(db: Session, payload: AskRequest) -> AskResponse:
    retrieved = retrieve_chunks(db, payload.question, settings.top_k_retrieval)
    print(f"[DEBUG] Retrieved chunks for question '{payload.question}': {retrieved}")
    prompt = build_ask_prompt(payload.question, payload.mode, retrieved)

    response = client.responses.create(
        model=settings.chat_model,
        input=prompt,
    )

    answer_text = response.output_text
    sources = [item["source_label"] for item in retrieved]
    related_concepts = []
    for item in retrieved:
        meta = item.get("metadata_json") or {}
        for concept in meta.get("related_concepts", []):
            if concept not in related_concepts:
                related_concepts.append(concept)

    db.add(
        AskLog(
            question=payload.question,
            mode=payload.mode,
            retrieved_chunk_ids=[item["chunk_id"] for item in retrieved],
            answer=answer_text,
        )
    )
    db.commit()

    suggested_practice = None
    for item in retrieved:
        meta = item.get("metadata_json") or {}
        practice = meta.get("suggested_practice")
        if practice:
            suggested_practice = practice
            break

    return AskResponse(
        answer=answer_text,
        sources=sources,
        related_concepts=related_concepts,
        suggested_practice=suggested_practice,
        disclaimer="Grounded AI-generated explanation based on retrieved app content.",
    )
