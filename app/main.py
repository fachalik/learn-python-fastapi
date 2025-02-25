from fastapi import FastAPI
from app.api.v1.router import router as api_router
from tortoise.contrib.fastapi import register_tortoise
from app.core.config import TORTOISE_ORM

app = FastAPI(title="FastAPI with Tortoise & PostgreSQL")

app.include_router(api_router, prefix="/api/v1")

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI with Tortoise-ORM!"}