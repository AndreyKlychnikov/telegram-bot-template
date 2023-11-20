from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.core.config import settings

engine = create_async_engine(
    settings.SQLALCHEMY_DATABASE_URI.unicode_string(),
    future=True,
)
SessionLocal = async_sessionmaker(
    engine,
    autoflush=False,
    expire_on_commit=False,
)


async def dispose_engine():
    await engine.dispose()
