from flask import request, render_template, abort
from jinja2 import TemplateNotFound
from application import simple_page
import africastalking
from flask import current_app as app

username = app.config.from_object('config.Config.USERNAME')
api_key = app.config.from_object('API_KEY')
africastalking.initialize(username, api_key)

sms = africastalking.SMS

@simple_page.route("/", methods=["GET","POST"])
def main():
    if request.method == "POST":
        sms_message = request.form['smsMessage']
        phone_number = request.form['phoneNumber']

        print(sms_message)
        print(phone_number)

        response = sms.send(sms_message,[phone_number])
        print(response)


    return render_template('index.html')

@simple_page.route('/simple', methods=["GET"])
def show():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)