from sqlalchemy.ext.hybrid import hybrid_property

from . import bcrypt, db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    email = db.Column(db.String(60))
    _password = db.Column(db.String(128))
    admin = db.Column(db.Boolean)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)