from contextlib import asynccontextmanager  # noqa: I001
from fastapi import FastAPI
from database import create_tables
from routes.reviews_route import router as review_router

@asynccontextmanager # with this we can control the lifespan of fastapi server like what task need to perform before server start or shutdown.
async def lifespan(app: FastAPI):
    create_tables()
    print("Database tables created")
    yield
    # Shutdown
    print("Shutting down the app")


app = FastAPI(
    title="Rangmanch Reviews API",
    description="Theater reviews API for Rangmanch platform",
    lifespan=lifespan
)

app.include_router(review_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Rangmanch Reviews API!"}
