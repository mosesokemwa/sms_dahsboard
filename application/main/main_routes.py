"""Routes for main pages."""
import os
import africastalking
from flask_login import login_required, current_user, login_user
from flask import current_app as app, Blueprint, render_template, request, flash, redirect, url_for


# from .assets import compile_main_assets
from .models import db, MessageStoreModel, UserModel
from .services import MessageService
from .forms import MessageForm, LoginForm, RegistrationForm


message_service = MessageService()
# Blueprint Configuration
main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates', static_folder='static')
# compile_main_assets(app)
username = os.getenv('USERNAME', 'sandbox')
api_key = os.getenv('API_KEY', 'fake')


africastalking.initialize(username, api_key)
sms = africastalking.SMS


@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = UserModel.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            error = 'Invalid username or password'
            # flash('Invalid username or password')
            # return redirect(url_for('main_bp.login', error=error))
            return render_template('auth/login.html', form=form, error=error)

        # login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('auth/login.html', form=form)


@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.all_messages'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        if user:
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main_bp.all_messages'))
    return render_template('auth/register.html', title='Register', form=form)


@main_bp.route('/', methods=['GET'])
def home():
    """Homepage route."""
    return render_template('index.html')


@main_bp.route('/about', methods=['GET', 'POST'])
@login_required
def main():
    if request.method == "POST":
        sms_message = request.form['smsMessage']
        phone_number = request.form['phoneNumber']
        response = sms.send(sms_message, [phone_number])

    return render_template('index.html')


@main_bp.route('/messages', methods=['GET', 'POST'])
@login_required
def all_messages():
    form = MessageForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # response = message_service.create_message()
            # print(response)
            flash('Message createion for email {}, text_message={}'.format(
                form.email.data, form.text_message.data))
            return redirect('/index')
    all_messages = message_service.get_all_messages()
    return render_template('message/messages.html', form=form, messages=all_messages)


@main_bp.route('/messages/create', methods=['GET', 'POST'])
@login_required
def create_messages():
    form = MessageForm()
    if form.validate_on_submit():
        # response = message_service.create_message()
        # print(response)
        flash('Message createion for email {}, text_message={}'.format(
            form.email.data, form.text_message.data))
        return redirect('/index')
    return render_template('message/create_message.html', form=form)


@main_bp.route('/subscribers', methods=['GET', 'POST'])
@login_required
def subscribers():
    pass


@main_bp.route('/subscribers/<int:id>', methods=['GET'])
@login_required
def subscriber(id):
    pass
