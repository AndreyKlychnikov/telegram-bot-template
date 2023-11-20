from sqlalchemy.ext.asyncio import AsyncSession


async def init_db(db: AsyncSession) -> None:
    # Create any database objects here
    ...
