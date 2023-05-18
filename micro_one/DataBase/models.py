from mongoengine import *

class Type(DynamicDocument):
    name = StringField(max_length=200)
    description = StringField(max_length=200)

