# Casting Agency API - Final Project
This API has been created to show my understanding in all of the topics that I have learnt while undertaking the Full Stack Web Development course through Udacity.

The Casting Agency company asked for an API to be created so that they can easily create and manage movies and actors on their database. The API will allow certain roles to perform various activites such as getting a list of the movies and actors, as well as adding new ones, updating current ones and deleting movies and actors from the data base. During each of these activities, the use must have the correct permissions to be able to carry out that activity.

@TODO: Need to add:
Info hosting instructions 
Instruction for setting up authentication so reviewers can test endpoints at live application endpoint

## Getting Started 
Installing Dependencies

## Python 3.7
Follow instructions to install the latest version of python on your platform in [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python) 

## Virtual Environment
We recommend using a virtual environment whenever using Python projects. To set up your virtual environment run:
```
python -m virtualenv
```
For windows:
```
source env/Scripts/activate
``` 
For mac:
```
source env/bin/activate
```

## Pip Dependencies
Once you have your virtual environment set up, install the dependencies by running 
```
pip install -r requirements.txt
```
which will install all of the required packages.

**Key Dependencies:**
- Flask: required to handle requests and responses.
- SQLAlchemy: The ORM used to handle the lightweight sqlite database. 
- Flask-CORS: used to handle cross origin requests from our frontend server.

## Database Setup
Create a new database in Postgres
```
createdb castingagency
```
With Postgres running, restore a database using the capstone.psql file provided by running:
```
psql castingagency < postgres.psql
```

## Setup of Variables
To set up your variables defined in your setup.sh, run as a source:
source setup.sh 

## Running the Server Locally
From within your current directory which contains the app.py file, to run the server and use developer mode
execute:
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
@TODO
## API Reference
The base URL is: 

## Error Handling 
- Errors are returned as JSON objects.
- The API will return 4 types of errors:    
    - 400: Bad request
    - 404: Resource not found
    - 405: Method not allowed
    - 422: Not processable
- The response for all errors will be in the following format:
```
{
  "error": "404",
  "message": "Resource not found",
  "success": false
}
```

## API Endpoints 
- GET '/actors'
- GET '/movies'
- POST '/actors'
- POST '/movies'
- PATCH '/actors/<id>'
- PATCH '/movies/<id>'
- DELETE '/actors/<id>'
- DELETE '/movies/<id>'

**GET '/actors'**
- Fetches a list of actors as an array of objects.
- Each object contains the information for an actor (name, age and gender).
- Requires the 'get:actors' permission
- Request Arguments: bearer token
- Returns: An object containing the actors and success value.
- Sample: curl http://127.0.0.1:5000/actors -H 'Authorization: Bearer <Token>'
```
{
    "actors": [
        {
            "age": 39,
            "gender": "Male",
            "id": 1,
            "name": "Chris Evans"
        },
        {
            "age": 55,
            "gender": "Male",
            "id": 2,
            "name": "Robert Downey, Jr"
        }
    ],
    "success": true
}
```

**GET '/movies'**
- Fetches a list of movies as an array of objects.
- Each object contains the information for a movie (title and release_date).
- Requires the 'get:movies' permission
- Request Arguments: bearer token
- Returns: An object containing the movies and success value.
- Sample: curl http://127.0.0.1:5000/movies -H "Authorization: Bearer <Token>"
```
{
    "movies": [
        {
            "id": 1,
            "release_date": "26th April 2012",
            "title": "The Avengers"
        },
        {
            "id": 2,
            "release_date": "26th April 2012",
            "title": "Avengers"
        }
    ],
    "success": true
}
```

**POST '/actors'**
- Posts a new actor to the database. It requires the name, age and gender 
for the actor. 
- Requires the 'post:actors' permission
- Request Arguments: name, age, gender, bearer token
- Returns: An object containing the actors (including the recently added 
actor) and success value.
- Sample: curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <Token>" -d '{"name":"John Smith","age":31,"gender":"Male"}' http://127.0.0.1:5000/actors  
```
{
    "actors": [
        {
            "age": 39,
            "gender": "Male",
            "id": 1,
            "name": "Chris Evans"
        },
        {
            "age": 55,
            "gender": "Male",
            "id": 2,
            "name": "Robert Downey, Jr"
        },
        {
            "age": 31,
            "gender": "Male",
            "id": 3,
            "name": "John Smith"
        }
    ],
    "success": true
}
```

**POST '/movies'**
- Posts a new movie to the database. It requires the title and release_date
for the movie. 
- Requires the 'post:movies' permission
- Request Arguments: title, release_date, bearer token
- Returns: An object containing the movies (including the recently added 
movie) and success value.
- Sample: curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <Token>" -d '{"title":"New Movie","release_date":"1st January 2021"}' http://127.0.0.1:5000/movies
```
{
    "movies": [
        {
            "id": 1,
            "release_date": "26th April 2012",
            "title": "The Avengers"
        },
        {
            "id": 2,
            "release_date": "26th April 2012",
            "title": "Avengers"
        },
        {
            "id": 3,
            "release_date": "1st January 2021",
            "title": "New Movie"
        }
    ],
    "success": true
}
```

**PATCH '/actors'**
- Updates an existing actor entry with the corresponding id in the database.
- Requires the 'patch:actors' permission
- Request Arguments: id, bearer token, and one or more of: name, age and gender
- Returns: An object containing the actors (showing the newly updated 
actor) and success value.
- Sample: curl -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer <Token>" -d '{"age":34}' http://127.0.0.1:5000/actors/3
```
{
    "actors": [
        {
            "age": 39,
            "gender": "Male",
            "id": 1,
            "name": "Chris Evans"
        },
        {
            "age": 55,
            "gender": "Male",
            "id": 2,
            "name": "Robert Downey, Jr"
        },
        {
            "age": 34,
            "gender": "Male",
            "id": 3,
            "name": "John Smith"
        }
    ],
    "success": true
}
```

**PATCH '/movies'**
- Updates an existing movie entry with the corresponding id in the database.
- Requires the 'patch:movies' permission
- Request Arguments: id, bearer token, and one or more of: title and release date
- Returns: An object containing the movies (showing the newly updated 
movie) and success value.
- Sample: curl -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer <Token>" -d '{"release_date":"31st February 2020"}' http://127.0.0.1:5000/movies/3
```
{
    "movies": [
        {
            "id": 1,
            "release_date": "26th April 2012",
            "title": "The Avengers"
        },
        {
            "id": 2,
            "release_date": "26th April 2012",
            "title": "Avengers"
        },
        {
            "id": 3,
            "release_date": "31st February 2020",
            "title": "New Movie"
        }
    ],
    "success": true
}
```

**DELETE '/actors'**
- Deletes an existing actor entry with the corresponding id in the database.
- Requires the 'delete:actors' permission
- Request Arguments: id, bearer token
- Returns: An object containing the actors (the actor with the corresponding
id will no longer appear) and success value.
- Sample: curl -X DELETE http://127.0.0.1:5000/actors/2 -H "Authorization: Bearer <Token>"
```
{
    "actors": [
        {
            "age": 39,
            "gender": "Male",
            "id": 1,
            "name": "Chris Evans"
        },
        {
            "age": 34,
            "gender": "Male",
            "id": 3,
            "name": "John Smith"
        }
    ],
    "success": true
}
```

**DELETE '/movies'**
- Deletes an existing movie entry with the corresponding id in the database.
- Requires the 'delete:movies' permission
- Request Arguments: id, bearer token
- Returns: An object containing the movies (the movie with the corresponding
id will no longer appear) and success value.
- Sample: curl -X DELETE http://127.0.0.1:5000/movies/2 -H "Authorization: Bearer <Token>"
```
{
    "movies": [
        {
            "id": 1,
            "release_date": "26th April 2012",
            "title": "The Avengers"
        },
        {
            "id": 3,
            "release_date": "31st February 2020",
            "title": "New Movie"
        }
    ],
    "success": true
}
```

## Testing 
To run the tests, run 
```
dropdb castingagencytest
createdb castingagencytest
psql castingagencytest < capstone.psql
python test_app.py
```

## Permissions
- get:actors -> Get access to the list of actors 
- get: movies -> Get access to the list of movies  
- post:actors -> Add a new actor
- post:movies -> Add a new movie
- patch:actor -> Update an actor
- patch:movie -> Update a movie
- delete:actor -> Delete an actor
- delete:movie -> Delete a movie

## Roles
- Casting Assistant
    - Can view actors and movies
- Casting Director 
    - Can view actors and movies
    - Add or delete an actor from the database
    - Update actors or movies
- Executive Producer
    - Can view actors and movies
    - Add or delete an actor from the database
    - Update actors or movies
    - Add or delete a movie from the database
