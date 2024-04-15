import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Register(Base):
    __tablename__ = 'register'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    username = Column(String(25), nullable=False)
    password = Column(String(25), nullable=False)
    # favorites = relationship('Favorites', backref='user', lazy=True)

class Login(Base):
    __tablename__ = 'login'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(25), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(25), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False) 

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, nullable=False)
    register_id = Column(Integer, ForeignKey('register.id'))
    # name = Column(String(250), nullable=False)
    # email = Column(String(250), nullable=False, unique=True)
    # password = Column(String(25), nullable=False)
    # favorites = relationship('Favorites', backref='user', lazy=True)

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    heigh = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)
    # favorites_person = relationship('FavoritesPerson', backref='person', lazy=True) #Preguntar'Favorites' o 'favorites'
    favorites = relationship('Favorites', backref='person', lazy=True)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(Integer)
    # favorites_planets = relationship('FavoritesPlanets', backref='planets', lazy=True) #Preguntar'Favorites' o 'favorites'
    favorites = relationship('Favorites', backref='planets', lazy=True)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    cargo = Column(Integer)
    passengers = Column(Integer)
    # favorites_vehicles = relationship('FavoritesVehicles', backref='vehicles', lazy=True) #Preguntar'Favorites' o 'favorites'
    favorites = relationship('Favorites', backref='vehicles', lazy=True)

# class Favorites(Base):
#     __tablename__ = 'favorites'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     # street_name = Column(String(250))
#     # street_number = Column(String(250))
#     # post_code = Column(String(250), nullable=False)
#     user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
#     user = relationship(User)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)
#     planets_id = Column(Integer, ForeignKey('planets.id'))
#     planets = relationship(Planets)
#     vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
#     vehicles = relationship(Vehicles)


class FavoritesPerson(Base):
    __tablename__ = 'favorites_person'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class FavoritesPlanets(Base):
    __tablename__ = 'favorites_planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    
class FavoritesVehicles(Base):
    __tablename__ = 'favorites_vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship(Vehicles)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
