from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Verse(Base):
    __tablename__ = "verses"

    id: Mapped[int] = mapped_column(primary_key=True)
    source_id: Mapped[int] = mapped_column(ForeignKey("sources.id", ondelete="CASCADE"), index=True)
    chapter_id: Mapped[int] = mapped_column(ForeignKey("chapters.id", ondelete="CASCADE"), index=True)
    chapter_number: Mapped[int] = mapped_column(Integer)
    verse_number: Mapped[int] = mapped_column(Integer)
    canonical_reference: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    sanskrit: Mapped[str] = mapped_column(Text)
    transliteration: Mapped[str] = mapped_column(Text)
    translation: Mapped[str] = mapped_column(Text)
    explanation: Mapped[str] = mapped_column(Text)
    life_application: Mapped[str] = mapped_column(Text)
