from telegram import Update

from app.core.config import settings
from app.services.analytics import tracker
from app.services.storage import DBStorage


@tracker.track_event("start")
async def start_handler(update: Update, _) -> None:
    """Inform user about what this bot can do"""
    storage = DBStorage()
    await storage.create_user(
        telegram_id=update.effective_user.id,
        chat_id=update.effective_chat.id,
        username=update.effective_user.username,
        first_name=update.effective_user.first_name,
        last_name=update.effective_user.last_name,
    )
    await update.message.reply_text(settings.ON_BOT_START_MESSAGE)


@tracker.track_event("help")
async def help_handler(update: Update, _) -> None:
    """Display a help message"""
    await update.message.reply_text(settings.ON_BOT_HELP_MESSAGE)
