#DJANGO

from django.db import models

class residents(models.Model):
    
    id = Column(Integer, primary_key=True, autoincrement=1)
    name = Column(String)
    age = Column(Integer)
    flat = Column(Integer)


#SQLAlchemy

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class residents(Base):
    __tablename__ = 'residents'
    
    id = Column(Integer, primary_key=True, autoincrement=1)
    name = Column(String)
    age = Column(Integer)
    flat = Column(Integer)


#Flask

from flask_restful import Resource, Api

class MyResource(Resource):
    def get(self):
        return {'message': 'Hello, World!'}

api = Api()
api.add_resource(MyResource, '/my_resource')



