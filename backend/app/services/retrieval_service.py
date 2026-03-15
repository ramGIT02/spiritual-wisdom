from sqlalchemy import text
from sqlalchemy.orm import Session

from app.services.embedding_service import create_embedding


def retrieve_chunks(db: Session, query: str, top_k: int = 6) -> list[dict]:
    embedding = create_embedding(query)

    sql = text(
        """
        SELECT
            cc.id,
            cc.entity_type,
            cc.entity_id,
            cc.source_label,
            cc.title,
            cc.content,
            cc.metadata_json,
            ce.embedding <=> CAST(:embedding AS vector) AS distance
        FROM content_embeddings ce
        JOIN content_chunks cc ON cc.id = ce.chunk_id
        ORDER BY ce.embedding <=> CAST(:embedding AS vector)
        LIMIT :top_k
        """
    )

    embedding_str = "[" + ",".join(str(x) for x in embedding) + "]"
    result = db.execute(sql, {"embedding": embedding_str, "top_k": top_k})

    items = []
    for row in result.mappings():
        items.append(
            {
                "chunk_id": row["id"],
                "entity_type": row["entity_type"],
                "entity_id": row["entity_id"],
                "source_label": row["source_label"],
                "title": row["title"],
                "content": row["content"],
                "metadata_json": row["metadata_json"],
                "distance": float(row["distance"]),
            }
        )
    return items
