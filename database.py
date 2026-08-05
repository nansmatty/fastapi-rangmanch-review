from sqlmodel import Session, SQLModel, create_engine

DATABASE_URL = "sqlite:///rangmanch_review.db"

engine = create_engine(DATABASE_URL, echo=True)


def create_tables():
    """Create the database tables based on the defined models."""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Dependency that provides a database session per request."""
    with Session(engine) as session:
        yield session
