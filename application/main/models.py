from application import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(UserMixin, db.Model):
    """Model for user accounts."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(200), primary_key=False, unique=False, nullable=False)
    admin = db.Column(db.Boolean, index=False, unique=False, nullable=False)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    last_login = db.Column(db.DateTime, index=False, unique=False, nullable=True)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class MessageStoreModel(db.Model):
    """Model for stored messages"""

    id = db.Column(db.Integer, primary_key=True)
    text_message = db.Column(db.String(140), nullable=False, unique=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    sent_boolean = db.Column(db.Boolean, default=False, nullable=False)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    last_login = db.Column(db.DateTime, index=False, unique=False, nullable=True)


class SubscribeModel(db.Model):
    """Model for stored subscribers details"""

    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.Integer, nullable=False, unique=False)
    email = db.Column(db.String(40), unique=False, nullable=True)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    last_login = db.Column(db.DateTime, index=False, unique=False, nullable=True)

