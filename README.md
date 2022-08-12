# Full Stack API Final Project


## Full Stack Trivia

# Trivia API

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out.

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1- Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.

2- Delete questions.

3- Add questions and require that they include question and answer text.

4- Search for questions based on a text query string.

5- Play the quiz game, randomizing either all questions or within a specific category.

## Getting Started 

### Pre-requisites and Local Development

Developers using this project should have the below packages installed:

- Python3 
- Pip 
- node 

#### Backend 
from the project main directory
cd backend 

once in the backend folder create and activate a virtualenv
```
python -m virtualenv env
source env/bin/activate
```
>**Note** - In Windows, the `env` does not have a `bin` directory. Therefore, you'd use the analogous command shown below:
```
source venv/Scripts/activate
```

then run ``` pip install requirements.txt``` All required packages are included in the requirements file.


To run the backend run the following commands:

```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
The application is run on  ``` http://127.0.0.1:5000/``` by default and is a proxy in the frontend configuration.



#### Frontend

The frontend of the trivia project uses NPM to manage software dependencies that relies on the package.json file located in the frontend directory of this repository. After cloning the application, open your terminal:
```
cd frontend 
```
run the below command to install the packages from the json file 

```
$ npm install
```
to run the frontend application run the below command 

```
$ npm start
```
once the frontend starts, on the browser urls goto
http://localhost:3000 to view the frontend. 


#### Tests

To run the tests, run

```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```


## API Reference

### Error Handling

Errors are returned as JSON objects in the following format:

```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}

{
    "success": False, 
    "error": 404,
    "message": "Page not found"
}

{
    "success": False, 
    "error": 422,
    "message": "unprocessable entity"
}

{
    "success": False, 
    "error": 500,
    "message": "Internal Server Error
}
```

The API will return three error types when requests fail:

400: Bad Request
404: Resource Not Found
422: Not Processable
500: Internal Server Error
405: Method Not Allowed

### Endpoints


**GET /categories**

General:
- get a list of categories

Curl Test: ```curl http://127.0.0.1:5000/categories```

```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true
}
```

**DELETE /questions/{id}**

General:
- Delete a question of the given ID if it exists. 
- on sucessful deleted, return success and the id of the deleted value.

Curl test: ```curl -X DELETE http://127.0.0.1:5000/questions/72 ```


```
{
  "success": true
}
```

**POST /questions/{id}**


General:
- Creates a new question using the submitted input field such as title, answer, category and difficulty. 
- on sucess, returns the id of the created question id, success value, total questions number.

Curl Test : ```curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":" who is the best football of the year 2021", "answer": "Lionel Messi","category" :"4", "difficulty":"2"}'```


```
{
  "created": 68, 
  "questions": [
    {
      "answer": "Tom Cruise", 
      "category": "5", 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Maya Angelou", 
      "category": "4", 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": "5", 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": "4", 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": "6", 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": "6", 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": "4", 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": "3", 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": "3", 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": "3", 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ], 
  "success": true, 
  "total_questions": 61
}
```


**POST /search**


General:
- search for a question using the submitted search term. 
- Returns the results base on pagination with a success value and the total number of questions.


Curl Test: ```curl http://127.0.0.1:5000/question/search -X POST -H "Content-Type: application/json" -d '{"searchTerm":" world bestt"}'```

```
{
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": "4", 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": "4", 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": "1", 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }
  ], 
  "success": true, 
  "total_questions": 3
}
```

**GET /categories/{id}/questions**


General:

- Returns a list of questions base on a pagination of 10 question per page


Curl Test: ```curl http://127.0.0.1:5000/categories/3/questions```

```
{
  "current_category": "Geography", 
  "questions": [
    {
      "answer": "Lake Victoria", 
      "category": "3", 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": "3", 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": "3", 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ], 
  "success": true, 
  "total_questions": 3
}
```

**POST /quizzes**

General:
- retrive question base on category
- returns the next question in the same category 

Curl Test: ``` curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"quiz_category":{"type":"Geography","id":"3"}, "previous_questions":[4]}'``` 


```
{
  "question": {
    "answer": "Agra", 
    "category": "3", 
    "difficulty": 2, 
    "id": 15, 
    "question": "The Taj Mahal is located in which Indian city?"
  }, 
  "success": true
}
```