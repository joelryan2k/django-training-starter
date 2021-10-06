To begin:

Install https://postgresapp.com/

```
    brew install python@3.8

    pip3.8 install pipenv

    git clone https://github.com/joelryan2k/django-training-starter.git

    git remote rm origin

    pipenv install

    pipenv shell

    ./scripts/generate-local-settings.sh
```

To deploy:
```
    dokku apps:create [name of your app]

    dokku config:set SECRET_KEY=`python -c "import secrets; print(secrets.token_urlsafe())"`

    dokku config:set DJANGO_SETTINGS_MODULE=main_project.settings.deployed

    dokku postgres:create [name of your app]-db

    dokku postgres:link [name of your app]-db [name of your app]

    dokku letsencrypt:enable

    git push dokku master

    dokku run python manage.py migrate

    dokku run python manage.py createsuperuser
```