from peewee import *
import datetime
from sqlite3 import *
db = SqliteDatabase('currency_mon_k.db')


class BaseModel(Model):
    class Meta:
        database = db


class Money(BaseModel):
    name_k = CharField(primary_key=True)
    koef = FloatField(null=False)
    
db.create_tables([Money], safe=True)
# 
#
#