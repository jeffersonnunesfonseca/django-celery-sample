# django-celery-sample

## Subir rabbitMq:

```bash
docker run -d \
  --name rabbitmq \
  --restart always \
  -p 5672:5672 \
  -p 15672:15672 \
  rabbitmq:3.13-management
```

## Start Server

```bash
 uv run manage.py runserver
```

## Start WORKER

```bash
celery -A proj worker -l info -Q produtos,estoque
```

## Producer

```bash
 uv run python producer.py
```
