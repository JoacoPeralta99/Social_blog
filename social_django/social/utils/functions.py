import os
from datetime import datetime

from django.utils.text import slugify
from django.conf import settings


def is_true(arg: str) -> bool:
    return str(arg).lower() in ('true', '1', 'yes', 't', 'y')


def normalize_filename(filename):
    filename, ext = os.path.splitext(filename)
    filename = slugify(filename).replace('-', '_')
    return f"{filename}{ext}"

def to_local_time(arg: datetime) -> str:
    return arg.strftime(settings.DATETIME_FORMAT)
