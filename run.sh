#!/bin/bash
source mivalle_env/bin/activate
python3 manage.py runserver &
sleep 5
xdg-open http://127.0.0.1:8000/
