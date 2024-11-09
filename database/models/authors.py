from peewee import IntegerField, CharField, BooleanField, ForeignKeyField

from database.models.base import BaseModel


class Authors(BaseModel):
    tg_id = IntegerField()


class AuthorsConfig(BaseModel):
    author_name = CharField()
    is_approved = BooleanField(default=False)
    is_admin = BooleanField(default=False)
    user = ForeignKeyField(Authors, backref="config")
