"""Routes for main pages."""
from flask import Blueprint, render_template, request
from flask import current_app as app
# from .assets import compile_main_assets
import africastalking

# Blueprint Configuration
main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')
# compile_main_assets(app)

username = app.config['USERNAME']
api_key = app.config['API_KEY']
africastalking.initialize(username, api_key)


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
    pass

@main_bp.route('/messages/<int:id>', methods=['GET'])
def messages(id):
    pass

@main_bp.route('/subscribers', methods=['GET', 'POST'])
def subscribers():
    pass

@main_bp.route('/subscribers/<int:id>', methods=['GET'])
def subscriber(id):
    pass
