# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
dropdb trivia && createdb trivia
```bash
psql trivia < trivia.psql
```

## Running the Backend Identified as the Server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## About End Points

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Response: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

GET '/questions'
- Fetches a list of all questions that ranges ten questions per pages governed by the request argument page
- Request Argument: page (int)
- Response: An object containing total questions, list of JSON formatted questions
{
    "categories": {
        "1": "Science", 
        "2": "Art", 
        "3": "Geography", 
        "4": "History", 
        "5": "Entertainment", 
        "6": "Sports"
    }, 
    "currentCategory": "-", 
    "questions": [
        {
            "answer": "Maya Angelou", 
            "category": 4, 
            "difficulty": 2, 
            "id": 5, 
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        }, 
        {
            "answer": "Muhammad Ali", 
            "category": 4, 
            "difficulty": 1, 
            "id": 9, 
            "question": "What boxer's original name is Cassius Clay?"
        }
    ], 
    "totalQuestions": 2
}

GET '/categories/<category_id>/questions'
- Fetches a list of questions for a category with id <category_id>
- Request Argument: category_id
- Response: An object containing total questions, list of JSON formatted questions as well as the currentCategory
{
    "currentCategory": "Geography", 
    "questions": [
            {
                "answer": "Lake Victoria", 
                "category": 3, 
                "difficulty": 2, 
                "id": 13, 
                "question": "What is the largest lake in Africa?"
            }, 
            {
                "answer": "The Palace of Versailles", 
                "category": 3, 
                "difficulty": 3, 
                "id": 14, 
                "question": "In which royal palace would you find the Hall of Mirrors?"
            }, 
            {
                "answer": "Agra", 
                "category": 3, 
                "difficulty": 2, 
                "id": 15, 
                "question": "The Taj Mahal is located in which Indian city?"
            }
        ], 
    "totalQuestions": 3
}


DELETE '/questions/<question_id>'
- Deletes the question that matches the question_id
- Request Arguments: <question_id>
- Response: A JSON object with the key 'success' to True if there was a successful deletion. If there was error, this renders a 422 response.
{
    "success": True
    'deleted':<question_id>
}

POST '/questions'
- creates a new question from the request body
- Request Content-Type: 'Application/json'
- Request Body: 
{
    "question" : " ",
    "answer": " ",
    "category": <category_id>,
    "difficulty": 1
}
- Response;  A JSON object with the key 'success' to True if there was a successful creation. If there were any errors, this renders a 404 response.

POST '/question/search'
- search a for a question by it's title
= Request Arguments: none
- Request Content-Type: 'Application/json'
- Request Body: 
{
    "searchTerm": "question title"
}
- Response: A JSON object that constains a list of questions found and the list of questions. If the question was not found, this renders a 404 response 
{
    "total_questions": len(questionResults),
    'success':True,
    "questions": questionResults,
    "currentCategory": '-'
}

- POST '/quizzes'
- get a random question from the list of all questions or by a category so long as the question does not match a list of previous questions
- Request Content-Type: 'Application/json'
- Request Body: 
{
    "previous_questions": [], 
    "quiz_category": {
        "id": id,
        "type": "type"
    }
}
- Response: A JSON object containing the a question that is not part of the previous queried question or an empty object if there are no more questions to be returned
{
    "question": {
        "question" : " ",
        "answer": " ",
        "category": category_id,
        "difficulty": 1
    }
}


- ERROR 400
- Response: Response with the following body:
{
    "success": False,
    "error": 400,
    "message": "Bad request"
}

- ERROR 404
- Response: Response with the following body:
{
    "success": False,
    "error": 404,
    "message": "Not Found"
}

- ERROR 422
- Response: Response with the following body:
{
    "success": False,
    "error": 422,
    "message": "Unprocessable entity"
}

- ERROR 500
- Response: Response with the following body:
{
    "success": False,
    "error": 500,
    "message": "server error"
}
```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```