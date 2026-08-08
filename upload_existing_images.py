import os
from pathlib import Path
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eventpr.settings")
django.setup()

from eventapp.models import Event
from django.core.files import File

BASE_DIR = Path(__file__).resolve().parent
MEDIA_DIR = BASE_DIR / "media"

for event in Event.objects.all():

    if not event.img:
        print(f"SKIP: {event.name} has no image")
        continue

    # Original database path, for example:
    # img/images_2_Aphdtfz.jpg
    filename = Path(event.img.name).name

    # Check possible old locations
    possible_files = [
        MEDIA_DIR / "img" / "pic" / filename,
        MEDIA_DIR / "img" / filename,
        MEDIA_DIR / "pic" / filename,
        BASE_DIR / "static" / "img" / filename,
    ]

    local_file = next(
        (path for path in possible_files if path.exists()),
        None
    )

    if not local_file:
        print(f"NOT FOUND: {event.name} -> {filename}")
        continue

    print(f"Uploading: {event.name}")
    print(f"Local file: {local_file}")

    with open(local_file, "rb") as f:
        event.img.save(filename, File(f), save=True)

    print(f"SUCCESS: {event.name}")
    print(f"Cloudinary URL: {event.img.url}")
    print("-" * 60)

print("Finished.")
