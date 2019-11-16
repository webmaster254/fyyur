from flask import Flask
from flask_migrate import Migrate
from . import create_fyyur_app, db

app = create_fyyur_app()


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

show_artists = db.Table('show_artists',
                              db.Column('artist_id', db.Integer, db.ForeignKey(
                                  'Artist.id'), primary_key=True),
                              db.Column('show_id', db.Integer, db.ForeignKey(
                                  'Show.id'), primary_key=True))


class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    show = db.relationship('Show')

    # TODO: implement any missing fields, as a database migration using Flask-Migrate


class Show(db.Model):
    __tablename__ = 'Show'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    date = db.Column(db.DateTime)
    image_link = db.Column(db.String(500))
    artist_id = db.relationship('Artist', secondary=show_artists)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'))


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate


# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
