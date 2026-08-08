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


@router.get("/", response_model=list[ReviewRead])
def list_reviews(play_name: str | None = Query(None, description="Filter by play name"), 
                 skip: int = Query(0, ge=0, description="Number to reviews to skip"),
                 limit: int = Query(10, ge=1, le=50, description="Max reviews to return"), 
                 session: Session = Depends(get_session)): # noqa: B008
    query = select(Review)

    if play_name:
        query = query.where(Review.play_name == play_name)

    query = query.offset(skip).limit(limit)

    reviews = session.exec(query).all()
    return reviews

