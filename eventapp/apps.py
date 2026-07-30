from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError


class EventappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eventapp'

    def ready(self):
        try:
            from .models import Event
            updated_count = 0
            for event in Event.objects.all():
                if event.img and event.img.name.startswith('pic/'):
                    event.img.name = event.img.name.replace('pic/', 'img/', 1)
                    event.save()
                    updated_count += 1
            if updated_count > 0:
                print(f"Successfully fixed {updated_count} image paths from pic/ to img/!")
        except (OperationalError, ProgrammingError):
            pass