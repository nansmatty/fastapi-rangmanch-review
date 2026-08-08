from fastapi import APIRouter, Depends, HTTPException, Query  # noqa: I001
from sqlmodel import Session, func, select
from database import get_session
from models import Review, ReviewCreate, ReviewRead, ReviewUpdate

router = APIRouter(prefix="/review", tags=["review"])

@router.post("/", response_model=ReviewRead)
def create_review(review: ReviewCreate, session: Session = Depends(get_session)):  # noqa: B008
    db_review = Review(**review.model_dump())
    session.add(db_review)
    session.commit()
    session.refresh(db_review)
    return db_review

