FROM python:3.8-slim

WORKDIR /usr/src/app

COPY . .

# Heroku doesn't support expose
#EXPOSE 8000

RUN useradd -m appuser && \
    chown -R appuser:appuser .

USER appuser    

RUN mkdir num_to_bin_clicker/config

ENV PATH=/home/appuser/.local/bin:$PATH

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir django==4.0 && \
    pip install django-environ --no-cache-dir && \
    pip install gunicorn && \
    pip install whitenoise

WORKDIR /usr/src/app

RUN echo DJANGO_SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key;print(get_random_secret_key())') > num_to_bin_clicker/config/.env && \
    echo DJANGO_DEBUG=TRUE >> num_to_bin_clicker/config/.env

WORKDIR /home/appuser/.local/bin

# CMD for local use
#CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

# CMD for Heroku
CMD gunicorn num_to_bin_clicker.wsgi:application --bind 0.0.0.0:$PORT