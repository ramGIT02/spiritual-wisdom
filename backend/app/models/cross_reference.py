from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class CrossReference(Base):
    __tablename__ = "cross_references"

    id: Mapped[int] = mapped_column(primary_key=True)
    from_verse_id: Mapped[int] = mapped_column(ForeignKey("verses.id", ondelete="CASCADE"), index=True)
    to_verse_id: Mapped[int] = mapped_column(ForeignKey("verses.id", ondelete="CASCADE"), index=True)
    relation_type: Mapped[str] = mapped_column(String(50), index=True)
    note: Mapped[str | None] = mapped_column(Text, nullable=True)
