# TODO - Create SQLAlchemy DB and Movie model
from flask import Flask, abort, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from src.repositories.movie_repository import movie_repository_singleton

db = SQLAlchemy()
class Movie(db.Model):
    movie_id = database.Column(database.Integer, primary_key = True)
    title = database.Column(database.String(40), nullable = False)
    director = database.Column(database.String(40), nullable = False)
    rating = database.Column(database.Integer, nullable = False)