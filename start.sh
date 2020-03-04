# start.sh

export FLASK_ENV=development
export APP_CONFIG_FILE=config.py
export FLASK_APP=wsgi.py
export FLASK_DEBUG=1
flask run