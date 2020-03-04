"""Routes for main pages."""
import os
from flask import Blueprint, render_template, request
from flask import current_app as app
# from .assets import compile_main_assets
import africastalking
from .models import db, MessageStoreModel
from faker import Faker
from datetime import datetime

fake = Faker()

# Blueprint Configuration
main_bp = Blueprint('main_bp', __name__, template_folder='templates', static_folder='static')
# compile_main_assets(app)
username = os.getenv('USERNAME', 'sandbox')
api_key = os.getenv('API_KEY', 'fake')


africastalking.initialize(username, api_key)
sms = africastalking.SMS

@main_bp.route('/', methods=['GET'])
def home():
    """Homepage route."""
    return render_template('index.html')


@main_bp.route('/about', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        sms_message = request.form['smsMessage']
        phone_number = request.form['phoneNumber']
        response = sms.send(sms_message,[phone_number])

    return render_template('index.html')

@main_bp.route('/messages', methods=['GET', 'POST'])
def messages():
    return render_template('messages.html', messages=MessageStoreModel.query.all())


@main_bp.route('/subscribers', methods=['GET', 'POST'])
def subscribers():
    pass

@main_bp.route('/subscribers/<int:id>', methods=['GET'])
def subscriber(id):
    pass
