from faker import Faker
from datetime import datetime

from .models import db, MessageStoreModel

fake = Faker()


class MessageService:
    def get_all_messages(cls):
        messages = MessageStoreModel.query.all()
        return messages

    def create_message(cls):



        # new_message = MessageStoreModel(text_message=fake.text(140),
        #                                 email=fake.email(),
        #                                 created_on=datetime.now())
        # db.session.add(new_message)  # Adds new User record to database
        # db.session.commit()
        return 'success'
