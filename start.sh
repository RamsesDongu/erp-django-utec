#!/usr/bin/env bash
celery -A core worker -l info --pool=solo &
gunicorn core.wsgi:application