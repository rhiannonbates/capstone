import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actors, Movies

TOKEN_ASSISTANT = os.environ.get('ASSISTANT')
TOKEN_DIRECTOR = os.environ.get('DIRECTOR')
TOKEN_PRODUCER = os.environ.get('PRODUCER')
TOKEN_EXPIRED = os.environ.get('EXPIRED_TOKEN')


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the Casting Agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ.get('DATABASE_URL_TEST')
        setup_db(self.app, self.database_path)

        # Sample new actor
        self.new_actor = {
            'name': 'Brie Larson',
            'age': 31,
            'gender': 'Female'
        }

        # Sample new movie
        self.new_movie = {
            'title': 'Avengers End Game',
            'release_date': '25th April 2019'
        }

        # Sample update actor
        self.update_actor = {
            'age': 21
        }

        # Sample update movie
        self.update_movie = {
            'title': 'New Movie'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
        pass

    '''
    Tests for getting actors
    '''

    def test_get_actors(self):
        """ This test represents successfully getting the list of actors """
        res = self.client().get('/actors',
                                headers={'AUTHORIZATION': TOKEN_ASSISTANT})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_405_actors_not_found(self):
        """ This test represents unsuccessfully getting the list of actors """
        res = self.client().get('/actors/1000',
                                headers={'AUTHORIZATION': TOKEN_ASSISTANT})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    '''
    Tests for getting movies
    '''

    def test_get_movies(self):
        """ This test represents successfully getting the list of movies """
        res = self.client().get('/movies',
                                headers={'AUTHORIZATION': TOKEN_DIRECTOR})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_405_movies_not_found(self):
        """ This test represents unsuccessfully getting the list of movies """
        res = self.client().get('/movies/1000',
                                headers={'AUTHORIZATION': TOKEN_DIRECTOR})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    '''
    Tests for adding actors
    '''

    def test_add_actor(self):
        """ This test represents successfully adding a new actor """
        res = self.client().post('/actors',
                                 headers={'AUTHORIZATION': TOKEN_DIRECTOR},
                                 json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_405_not_allowed_to_add_actor(self):
        """ This test represents unsuccessfully adding a new actor """
        res = self.client().post('/actors/1000',
                                 headers={'AUTHORIZATION': TOKEN_DIRECTOR},
                                 json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    '''
    Tests for adding movies
    '''

    def test_add_movie(self):
        """ This test represents successfully adding a new movie """
        res = self.client().post('/movies',
                                 headers={'AUTHORIZATION': TOKEN_PRODUCER},
                                 json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_405_not_allowed_to_add_movie(self):
        """ This test represents unsuccessfully adding a new movie """
        res = self.client().post('/movies/1000',
                                 headers={'AUTHORIZATION': TOKEN_PRODUCER},
                                 json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    '''
    Tests for updating an actor's details
    '''

    def test_update_actor(self):
        """ This test represents successfully updating an actor """
        res = self.client().patch('/actors/1',
                                  headers={'AUTHORIZATION': TOKEN_DIRECTOR},
                                  json=self.update_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_422_actor_doesnt_exist_to_update(self):
        """ This test represents an actor that does not exist that is
        to be updated """
        res = self.client().delete('/actors/1000',
                                   headers={'AUTHORIZATION': TOKEN_DIRECTOR},
                                   json=self.update_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    '''
    Tests for updating a movie
    '''

    def test_update_movie(self):
        """ This test represents successfully updating a movie """
        res = self.client().patch('/movies/2',
                                  headers={'AUTHORIZATION': TOKEN_PRODUCER},
                                  json=self.update_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_422_movie_doesnt_exist_to_update(self):
        """ This test represents if the movie does not exist that is to
        be updated """
        res = self.client().delete('/movies/1000',
                                   headers={'AUTHORIZATION': TOKEN_PRODUCER},
                                   json=self.update_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    '''
    Tests for deleting an actor
    '''

    def test_delete_actor(self):
        """ This test represents successfully deleting an actor """
        res = self.client().delete('/actors/2',
                                   headers={'AUTHORIZATION': TOKEN_PRODUCER})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_422_actor_doesnt_exist_to_delete(self):
        """ This test represents if the actor does not exist that is to
        be deleted """
        res = self.client().delete('/actors/1000',
                                   headers={'AUTHORIZATION': TOKEN_PRODUCER})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    '''
    Tests for deleting a movie
    '''

    def test_delete_movie(self):
        """ This test represents successfully deleting a movie """
        res = self.client().delete('/movies/2',
                                   headers={'AUTHORIZATION': TOKEN_PRODUCER})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_422_movie_doesnt_exist_to_delete(self):
        """ This test represents if the movie does not exist that is to
        be deleted """
        res = self.client().delete('/movies/1000',
                                   headers={'AUTHORIZATION': TOKEN_PRODUCER})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    '''
    Tests for role permissions
    '''

    def test_401_incorrect_permissions_to_update_movie(self):
        """ This test represents not having the correct permissions to update
        a movie """
        res = self.client().post('/movies',
                                 headers={'AUTHORIZATION': TOKEN_ASSISTANT},
                                 json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_401_no_permission_add_actor(self):
        """ This test represents not having a token present """
        res = self.client().post('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'],
                         'Authorization header is expected.')

    def test_404_token_expired_get_actor(self):
        """ This test represents token having expired for user """
        res = self.client().get('/actors',
                                headers={'AUTHORIZATION': TOKEN_EXPIRED})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'token_expired')
        self.assertEqual(data['description'], 'Token expired.')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
