from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Practice(Base):
    __tablename__ = "practices"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    tradition: Mapped[str] = mapped_column(String(100), index=True)
    duration_minutes: Mapped[int] = mapped_column(Integer)
    purpose: Mapped[str] = mapped_column(Text)
    benefits: Mapped[str] = mapped_column(Text)
    common_mistakes: Mapped[str] = mapped_column(Text)
