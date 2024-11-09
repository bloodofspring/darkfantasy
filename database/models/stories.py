from peewee import CharField, ForeignKeyField, BooleanField

from database.models.authors import Authors
from database.models.base import BaseModel


class Stories(BaseModel):
    name = CharField()
    file_name = CharField()
    reserve_storage = CharField()

    is_approved = BooleanField()
    is_posted = BooleanField()

    author = ForeignKeyField(Authors, backref="stories")
