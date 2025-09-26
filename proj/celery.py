import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")

app = Celery("proj")

# Configura Celery lendo settings do Django
app.config_from_object("django.conf:settings", namespace="CELERY")

# Descobre tasks
app.autodiscover_tasks()
