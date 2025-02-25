from app.core.config import TORTOISE_ORM
from tortoise import Tortoise, run_async

async def init_db():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()

async def close_db():
    await Tortoise.close_connections()
