from mongoengine import *
class User(Document):
    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    balance = IntField(min_value=0, default=0)
    credit = IntField(min_value=0, default=0)
