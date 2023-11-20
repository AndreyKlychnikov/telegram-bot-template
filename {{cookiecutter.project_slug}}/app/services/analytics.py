from amplitude import Amplitude, BaseEvent
from telegram import Update

from app.core.config import settings
from app.utils import SingletonMeta


class AmplitudeService(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.client = Amplitude(settings.AMPLITUDE_TOKEN)

    def track_error(self, user_id: str, error_text: str):
        self.client.track(
            BaseEvent(
                event_type="error",
                user_id=user_id,
                event_properties={"error_text": error_text},
            )
        )

    def track_event(self, event_name):
        """Decorator for tracking events in Amplitude."""

        def decorator(func):
            def wrapper(update: Update, *args, **kwargs):
                user_id = str(update.effective_user.id)
                self.client.track(
                    BaseEvent(
                        event_type=event_name,
                        user_id=user_id,
                    )
                )
                try:
                    result = func(update, *args, **kwargs)
                except Exception as e:
                    self.track_error(user_id, str(e))
                    raise e
                return result

            return wrapper

        return decorator


tracker = AmplitudeService()
