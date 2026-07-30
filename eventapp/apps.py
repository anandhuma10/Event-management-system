from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError

class EventappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eventapp'

    def ready(self):
        try:
            from django.contrib.auth.models import User
            # Check if a superuser already exists
            if not User.objects.filter(is_superuser=True).exists():
                User.objects.create_superuser('Event', 'admin@example.com', 'Event')
                print("Superuser 'Event' created successfully!")
        except (OperationalError, ProgrammingError):
            pass