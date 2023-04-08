from models import Movie
from app import database
class MovieRepository:
    def get_all_movies(self):
        # TODO get all movies from the DB
        #Queries database and grabs all info
        findMovies = Movie.query.all()  
        return findMovies

    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID
        #Queries database to find movie using movie_id
        findMovies = Movie.query.get(movie_id)
        return None

    def create_movie(self, title, director, rating):
        # TODO create a new movie in the DB
        #Takes requested inputs, adds them to database, then commits it to the database
        makeMovies = Movie(title=title,director=director,rating=rating)
        db.session.add(makeMovies)
        db.session.commit()
        return makeMovies

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        #Queries the movie table, filtering by the title and titles like what was requested and grabs all
        findMovies = Movie.query.filter(Movie.title.ilike(f'%{title}%')).all()
        return findMovies


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
