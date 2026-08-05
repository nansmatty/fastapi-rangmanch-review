from datetime import datetime  # noqa: I001
from typing import Optional
from sqlmodel import Field, SQLModel


class Review(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # noqa: UP045
    play_name: str = Field(index=True)
    reviewer_name: str
    rating: int = Field(ge=1, le=5)
    comment: str
    created_at: datetime = Field(default_factory=datetime.now)


class ReviewCreate(SQLModel):
    play_name: str
    reviewer_name: str
    rating: int = Field(ge=1, le=5)
    comment: str


class ReviewRead(SQLModel):
    id: int
    play_name: str
    reviewer_name: str
    rating: int
    comment: str
    created_at: datetime


class ReviewUpdate(SQLModel):
    rating: Optional[int] = Field(default=None, ge=1, le=5)  # noqa: UP045
    comment: Optional[str] = None  # noqa: UP045
