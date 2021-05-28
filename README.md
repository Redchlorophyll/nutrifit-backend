# nutrifit-backend

nutrifit-backend is rest api created with django rest. this repository originally for bangkit 2021 Capstone Project

# Installation

clone this project first

```bash
git clone https://github.com/Redchlorophyll/nutrifit-backend.git
```

create virtuaelnv and activate your virtualenv

```bash
virtualenv virtualenv_name
source virtualenv_name/bin/activate
```

in your terminal cd to project folder

```bash
cd nutrifit_backend
```

install all libraries in requirements.txt

```bash
pip install -r requirements.txt
```

migrate the database

```bash
python manage.py makemigrations
python manage.py migrate
```

start your local Server

```bash
python manage.py runserver
```

# credential

this project require credential.json. you can get it from service account in your GCP project.

# endpoint documentation

[API documentation on bahasa indonesia (docs)](https://docs.google.com/document/d/1EeH0tcAX-J_keGM-7HH-Pztz-hrvbwxeh76ZqeRjcnU/edit?usp=sharing)
