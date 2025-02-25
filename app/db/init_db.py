import asyncio
from app.db.config import init_db

if __name__ == "__main__":
    asyncio.run(init_db())
