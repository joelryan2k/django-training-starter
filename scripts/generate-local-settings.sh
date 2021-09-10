#!/bin/bash 
echo "SECRET_KEY = '`python -c "import secrets; print(secrets.token_urlsafe())"`'" > ./main_project/settings/local_settings.py
