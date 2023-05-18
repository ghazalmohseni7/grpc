from mongoengine import *

class Event(DynamicDocument):
    name = StringField(max_length=200)
    description = StringField(max_length=200)
    created_time=StringField(max_length=200)

