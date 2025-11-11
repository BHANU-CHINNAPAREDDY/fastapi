from typing import Optional

from sqlalchemy import Index, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass


class MetalPriceGold(Base):
    __tablename__ = 'metal_price_gold'
    __table_args__ = (
        Index('ix_metal_price_gold_hashcolumn', 'hashcolumn', unique=True),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    country: Mapped[Optional[str]] = mapped_column(String(250))
    city: Mapped[Optional[str]] = mapped_column(String(250))
    currency: Mapped[Optional[str]] = mapped_column(String(250))
    gold_24k: Mapped[Optional[str]] = mapped_column(String(250))
    gold_22k: Mapped[Optional[str]] = mapped_column(String(250))
    gold_18k: Mapped[Optional[str]] = mapped_column(String(250))
    gold_24k_inr: Mapped[Optional[str]] = mapped_column(String(250))
    gold_22k_inr: Mapped[Optional[str]] = mapped_column(String(250))
    gold_18k_inr: Mapped[Optional[str]] = mapped_column(String(250))
    date_scraped: Mapped[Optional[str]] = mapped_column(String(250))
    hashcolumn: Mapped[Optional[str]] = mapped_column(String(32))


class MetalPriceSilverAndPlatinum(Base):
    __tablename__ = 'metal_price_silver_and_platinum'
    __table_args__ = (
        Index('ix_metal_price_silver_and_platinum_hashcolumn', 'hashcolumn', unique=True),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    country: Mapped[Optional[str]] = mapped_column(String(250))
    city: Mapped[Optional[str]] = mapped_column(String(250))
    currency: Mapped[Optional[str]] = mapped_column(String(250))
    silver_10gm_price: Mapped[Optional[str]] = mapped_column(String(250))
    platinum_10gm_price: Mapped[Optional[str]] = mapped_column(String(250))
    date_scraped: Mapped[Optional[str]] = mapped_column(String(250))
    hashcolumn: Mapped[Optional[str]] = mapped_column(String(32))
