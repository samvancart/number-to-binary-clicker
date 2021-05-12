# Number to Binary Clicker
This app was created as part of an exercise for the University of Helsinki's course Devops with Docker. The app is written in Python using the Django framework.
# Prerequisites
[Python](https://www.python.org/downloads/) 3.8
[Pip](https://pip.pypa.io/en/stable/installing/)
# Clone project
Clone the project into a directory with the command `git clone https://github.com/samvancart/number-to-binary-clicker.git`
# Create config file
Navigate into project root directory with `cd /number-to-binary-clicker`
Create config file with `mkdir /num_to_bin_clicker/config`
# Install Django and libs
Download django or skip if already installed: `pip install django==3.1`
`pip install django-environ`
# Generate environment variables
run `echo DJANGO_SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())') > /num_to_bin_clicker/config/.env`
run `echo DJANGO_DEBUG=TRUE >> /num_to_bin_clicker/config/.env`
# Run
run with command `python manage.py runserver`
or `python3 manage.py runserver`
Server will start at http://localhost:8000/clicker