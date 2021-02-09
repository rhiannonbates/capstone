import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Movies, Actors
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Header',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    '''
    Method to get the list of all actors in the database
    '''

    def get_actors():
        actors_all = Actors.query.order_by(Actors.id).all()
        actors = [actor.format() for actor in actors_all]

        return actors

    '''
    Method to get the list of all movies in the database
    '''

    def get_movies():
        movies_all = Movies.query.order_by(Movies.id).all()
        movies = [movie.format() for movie in movies_all]

        return movies

    '''
    Get /
        Get initial page to ensure the api is working
    '''

    @app.route('/', methods=['GET'])
    def main():
        return jsonify({'message': 'Welcome to Casting Agency API'})

    '''
    GET /actors
        Requires 'get:actors' permission
        Returns status code 200 and json {'success': true, 'actors': actors}
        where actors are the list of actors or an appropriate status code
        indicating reason for failure.
    '''

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def display_actors(payload, *args, **kwargs):
        try:
            actors = get_actors()
            return jsonify({
                "success": True,
                "actors": actors
            })
        except Exception:
            abort(400)

    '''
    GET /movies
        Requires 'get:movies' permission
        Returns status code 200 and json {'success': true, 'movies': movies}
        where movies are the list of movies or an appropriate status code
        indicating reason for failure.
    '''

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def display_movies(payload, *args, **kwargs):
        try:
            movies = get_movies()
            return jsonify({
                "success": True,
                "movies": movies
            })
        except Exception:
            abort(400)

    '''
    POST /actors
        Creates a new entry in the Actors data table
        It requires 'post:actor' permission
        Returns status code 200 and json {'success': true, 'actors': actors}
        where actors are the list of actors or an appropriate status code
        indicating reason for failure.
    '''

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def add_actor(payload, *args, **kwargs):
        body = request.get_json()
        name = body.get('name')
        age = body.get('age')
        gender = body.get('gender')
        try:
            new_actor = Actors(name=name, age=age, gender=gender)
            new_actor.insert()

            actors = get_actors()
            return jsonify({
                "success": True,
                "actors": actors
            })
        except Exception:
            abort(400)

    '''
    POST /movies
        Creates a new entry in the Actors data table
        It requires 'post:movie' permission
        Returns status code 200 and json {'success': true, 'movies': movies}
        where movies are the list of movies or an appropriate status code
        indicating reason for failure.
    '''

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def add_movie(payload, *args, **kwargs):
        body = request.get_json()
        title = body.get('title')
        release_date = body.get('release_date')
        try:
            new_movie = Movies(title=title, release_date=release_date)
            new_movie.insert()

            movies = get_movies()
            return jsonify({
                "success": True,
                "movies": movies
            })
        except Exception:
            abort(400)

    '''
    PATCH /actors/<id>
        It should update the required row for <id>
        It requires 'patch:actor' permission
        Returns status code 200 and json {'success': true, 'actors': actors}
        where actors are the list of actors or an appropriate status code
        indicating reason for failure.
    '''

    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def update_actor(jwt, id):
        try:
            actor = Actors.query.filter(Actors.id == id).one_or_none()
            if actor is None:
                abort(404)

            body = request.get_json()
            new_name = body.get('name', actor.name)
            new_age = body.get('age', actor.age)
            new_gender = body.get('gender', actor.gender)

            actor.name = new_name
            actor.age = new_age
            actor.gender = new_gender
            actor.update()

            actors = get_actors()
            return jsonify({
                "success": True,
                "actors": actors
            })
        except Exception:
            abort(422)

    '''
    PATCH /movies/<id>
        It should update the required row for <id>
        It requires 'patch:movie' permission
        Returns status code 200 and json {'success': true, 'movies': movies}
        where movies are the list of movies or an appropriate status code
        indicating reason for failure.
    '''

    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def update_movie(jwt, id):
        try:
            movie = Movies.query.filter(Movies.id == id).one_or_none()
            if movie is None:
                abort(404)

            body = request.get_json()
            new_title = body.get('title', movie.title)
            new_release_date = body.get('release_date', movie.release_date)

            movie.title = new_title
            movie.release_date = new_release_date
            movie.update()

            movies = get_movies()
            return jsonify({
                "success": True,
                "movies": movies
            })
        except Exception:
            abort(422)

    '''
    DELETE /actors/<id>
        It should delete the row for <id>
        It requires 'delete:actor' permission
        Returns status code 200 and json {'success': true, 'actors': actors}
        where actors are the list of actors or an appropriate status code
        indicating reason for failure.
    '''

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(jwt, id):
        try:
            actor = Actors.query.filter(Actors.id == id).one_or_none()
            if actor is None:
                abort(404)

            actor.delete()

            actors = get_actors()
            return jsonify({
                "success": True,
                "actors": actors
            })
        except Exception:
            abort(422)

    '''
    DELETE /movies/<id>
        It should delete the row for <id>
        It requires 'delete:movies' permission
        Returns status code 200 and json {'success': true, 'movies': movies}
        where movies are the list of movies or an appropriate status code
        indicating reason for failure.
    '''

    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(jwt, id):
        try:
            movie = Movies.query.filter(Movies.id == id).one_or_none()
            if movie is None:
                abort(404)

            movie.delete()

            movies = get_movies()
            return jsonify({
                "success": True,
                "movies": movies
            })
        except Exception:
            abort(422)

    # ERROR HANDLING
    '''
    Error handler for 422
    '''

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
                        "success": False,
                        "error": 422,
                        "message": "unprocessable"
                        }), 422

    '''
    Error handler for 405
    '''

    @app.errorhandler(405)
    def unprocessable(error):
        return jsonify({
                        "success": False,
                        "error": 405,
                        "message": "method not allowed"
                        }), 405

    '''
    Error handler for 404
    '''

    @app.errorhandler(404)
    def noresource(error):
        return jsonify({
                        "success": False,
                        "error": 404,
                        "message": "resource not found"
                        }), 404

    '''
    Error handler for 400
    '''

    @app.errorhandler(400)
    def badrequest(error):
        return jsonify({
                        "success": False,
                        "error": 400,
                        "message": "bad request"
                        }), 400

    '''
    Error handler for AuthError
    '''

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        """
        Receive the raised authorization error and propagates it as response
        """
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
