# Casting Agency API - Final Project
This API has been created to show my understanding in all of the topics that I have learnt while undertaking the Full Stack Web Development course through Udacity.

The Casting Agency company asked for an API to be created so that they can easily create and manage movies and actors on their database. The API will allow certain roles to perform various activites such as getting a list of the movies and actors, as well as adding new ones, updating current ones and deleting movies and actors from the data base. During each of these activities, the use must have the correct permissions to be able to carry out that activity.

## Getting Started 
Installing Dependencies

## Python 3.7
Follow instructions to install the latest version of python on your platform in [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python) 

## Virtual Environment
We recommend using a virtual environment whenever using Python projects. To set up your virtual environment run:
```
python -m virtualenv env
source env/bin/activate
```
Note for windows the env folder does not have a bin directory so use:
```
source env/Scripts/activate
``` 

## Pip Dependencies
Once you have your virtual environment set up, install the dependencies by running 
```
pip3 install -r requirements.txt
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

## API Reference
The base URL is: https://capstone-bates.herokuapp.com/ 

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
- Sample: curl https://capstone-bates.herokuapp.com/actors -H 'Authorization: Bearer <Token>'
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
- Sample: curl https://capstone-bates.herokuapp.com/movies -H "Authorization: Bearer <Token>"
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
- Sample: curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <Token>" -d '{"name":"John Smith","age":31,"gender":"Male"}' https://capstone-bates.herokuapp.com/actors  
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
- Sample: curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <Token>" -d '{"title":"New Movie","release_date":"1st January 2021"}' https://capstone-bates.herokuapp.com/movies
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
- Sample: curl -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer <Token>" -d '{"age":34}' https://capstone-bates.herokuapp.com/actors/3
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
- Sample: curl -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer <Token>" -d '{"release_date":"31st February 2020"}' https://capstone-bates.herokuapp.com/movies/3
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
- Sample: curl -X DELETE https://capstone-bates.herokuapp.com/actors/2 -H "Authorization: Bearer <Token>"
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
- Sample: curl -X DELETE https://capstone-bates.herokuapp.com/movies/2 -H "Authorization: Bearer <Token>"
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

## Testing locally
To run the tests, run 
```
dropdb castingagencytest
createdb castingagencytest
psql castingagencytest < capstone.psql
python test_app.py
```

## Testing Heroku endpoints on Postman
Import the collection ```./CapstoneProject.postman_collection.json``` and run the collection. 

## Authorization Tokens
ASSISTANT = 'bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNUTS14U1BlZ1ZqT2paZTREdXBoSiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYmF0ZXMuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMWFiZWM4MGQzY2UyMDA3MDRlNTcxYyIsImF1ZCI6ImNhc3RpbmdBZ2VuY3lBUEkiLCJpYXQiOjE2MTI3NzkzNDQsImV4cCI6MTYxMjc4NjU0NCwiYXpwIjoid3NjUW1PTzVta1A5dWFubVdrV1lvY0h3MWtQWkNjY3EiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.JWjjD3NxLlVNL4HPG0KMwUGQIQL_HsHnkduCj0fy7FzDpr96SI4P1RQCFCp5afeUrUCGpEqo_H1zzpbeFje-Mayl0_ZgJcBP-LI5cvdcdc3OdfHncdUbis1s06YnI6ZDa98szs47B4kzVwbyTadGLJ_m5WiqtJGPSGH_r9gaS8_Az3O2tZrZq6IyBqymgerE0cF4po7WE7FbyviT-tMgqyccxcSLzF5hXYT1iIoC_uKl1TBasWnbwDWZmx3nBvM_1HxAb7J7kEEpzE1Zzdyl65rQOkzqO0Z7H8_73ga6cREDCorE3rZsbsVocoMjWaonhzIj6lz-YCQKJSNb9g1vyA'
DIRECTOR = 'bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNUTS14U1BlZ1ZqT2paZTREdXBoSiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYmF0ZXMuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMWFiZWViYjEyZmMzMDA2ODNmYTc4ZCIsImF1ZCI6ImNhc3RpbmdBZ2VuY3lBUEkiLCJpYXQiOjE2MTI3NzkyODksImV4cCI6MTYxMjc4NjQ4OSwiYXpwIjoid3NjUW1PTzVta1A5dWFubVdrV1lvY0h3MWtQWkNjY3EiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3JzIl19.TZmeZ5HQ_uCm6ZY-RlpRehr_lsfbIjZeHsi-kCHpxiYMaxT3SKzj115E9NAj8gxTeht36E0pvYWtbNM2QMNc8AhnC166Q1vmWWmDQFmTJhv7RaPi190wTz82_L__thIMRYy-TFoTyJ4M3SqbYp-HWlOAWvyjClRDMtGg453ZYbEcBnePw3As3o6os19oh8TaQ7SMJ8aa8rvZkZQQC_lSDDpOmJQtoaUWXOs3W5EmXrMBCE5w7s6eo4jtb0fK7AwXUd8pQzbLj8X-2Ux3sypEKWkuX4cUhKWX30lI7fz8EQt0w0mM6hcyLoP3l28LvJorFNbHQ3G9H_LEBGw754Cwbg'
PRODUCER = 'bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNUTS14U1BlZ1ZqT2paZTREdXBoSiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYmF0ZXMuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmZjU3M2M3ZmE5ZTM5MDA2ZmI3Y2I1NSIsImF1ZCI6ImNhc3RpbmdBZ2VuY3lBUEkiLCJpYXQiOjE2MTI3NzkyMzQsImV4cCI6MTYxMjc4NjQzNCwiYXpwIjoid3NjUW1PTzVta1A5dWFubVdrV1lvY0h3MWtQWkNjY3EiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.dWUx6TKTHa3WTYlFmquZAx0Ei7CkqhguNPJRLuAOKHpXjsHvgUEHac5sQ3P0VctLdr5LKDPML1UKlLiAcCsrRW4kAa85jWrcV6476Tw3Rd668ygIDuICzrlWnAvt7i9zDC1vfzhdqTaQEPLCP9gPwbDVxSpUllWl3LC3FnRyEhSdKPKy89Njypvj4yUZ34Qk4asvsr8H-_HrZs2FAQLExNmyCDz_8r1IdvFjtRYNwE0XH6FM3AOj9SLz1aLEaZJLt03EglXNum2413c3WcsHI-vvssx_2hTQ5t5ipVBeHU9OZVjwC7PRhbIOBB0EF32qTe4jLgJ2xCEoQWCGjLol3g'

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
