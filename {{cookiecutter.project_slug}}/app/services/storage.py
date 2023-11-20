from functools import wraps

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import SessionLocal
from app.models.base import User


def session_provider(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        async with SessionLocal() as session:
            return await func(session, *args, **kwargs)

    return wrapper


class DBStorage:
    @staticmethod
    @session_provider
    async def create_user(
        session: AsyncSession,
        telegram_id: int,
        chat_id: int,
        username: str,
        first_name: str,
        last_name: str,
    ) -> User:
        query = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        user = query.scalar_one_or_none()
        if user:
            return user
        user = User(
            telegram_id=telegram_id,
            chat_id=chat_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        session.add(user)
        await session.commit()
        return user
