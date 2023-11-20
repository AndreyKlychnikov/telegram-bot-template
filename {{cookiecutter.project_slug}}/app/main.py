import logging

import sentry_sdk
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
)

from app.core.config import TelegramBotMode
from app.core.config import settings
from app.handlers.base import start_handler, help_handler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def post_init(application: Application) -> None:
    await application.bot.set_my_commands(
        [
            ("start", "Starts the bot"),
            ("help", "Shows help message"),
        ]
    )


def init_app():
    application = (
        Application.builder()
        .token(settings.TELEGRAM_TOKEN)
        .post_init(post_init)
        .build()
    )
    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("help", help_handler))
    return application


def init_sentry():
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        traces_sample_rate=0,
        profiles_sample_rate=0,
    )


def run_polling() -> None:
    application = init_app()
    application.run_polling(allowed_updates=Update.ALL_TYPES)


def run_webhook() -> None:
    application = init_app()
    application.run_webhook(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    logging.info("Starting bot...")
    init_sentry()
    if settings.TELEGRAM_MODE == TelegramBotMode.WEBHOOK:
        run_webhook()
    else:
        run_polling()
