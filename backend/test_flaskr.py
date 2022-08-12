from email.quoprimime import body_check
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category
from urllib import response
from flask import Response


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
            "question": "question 1 to answer",
            "answer": "answer to question 1",
            "difficulty": 3,
            "category": 1
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """ Executed after reach test """
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_paginated_questions(self):
        response = self.client().get("/questions")
        body = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(body['success'], True)
        self.assertTrue(len(body["questions"]))
        self.assertTrue(body["total_questions"])
        self.assertTrue(len(body["categories"]))

    def test_404_sent_requesting_questions_beyond_pages(self):
        response = self.client().get('/questions?page=1000')
        body = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(body['success'], False)
        self.assertEqual(body['message'], 'Page not found')

    def test_get_categories(self):
        response = self.client().get("/categories")
        self.assertEqual(response.status_code, 200)
        body = json.loads(response.data)

        self.assertTrue(len(body["categories"]))
        self.assertIsNotNone(body["categories"])

    def test_404_requesting_non_existing_category(self):
        response = self.client().get('/categories/100000')
        body = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(body['success'], False)
        self.assertEqual(body['message'], 'Page not found')

    '''
        Delete session test case
    '''
    # note id need to be change for every test to avoid failure of test

    def test_delete_question(self):
        id = 66
        response = self.client().delete(f'/questions/{id}')
        body = json.loads(response.data)
        question = Question.query.filter(Question.id == id).one_or_none()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(body['success'], True)
        self.assertEqual(body['deleted'], id)
        self.assertEqual(question, None)

    def test_422_question_not_exits(self):
        response = self.client().delete('/questions/1000')
        body = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertEqual(body['success'], False)
        self.assertEqual(body['message'], 'unprocessable entity')

    '''
        search section test case
    '''

    def test_search_question(self):
        data = json.dumps({"searchTerm": "questionSearch"})
        response = self.client().post(
            "/questions/search",
            data=data,
            content_type="application/json")
        body = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(body['success'], True)
        self.assertIsNotNone(body['questions'])
        self.assertIsNotNone(body['total_questions'])

    def test_404_for_bad_search_request(self):
        new_search = {
            "searchTerm": "notaquestion",
        }
        response = self.client().post(
            "/questionsearch",
            data=json.dumps(new_search),
            content_type="application/json")
        self.assertEqual(response.status_code, 404)

        body = json.loads(response.data)
        self.assertEqual(body["message"], "Page not found")

    '''
        Add section test case
    '''

    def test_add_question(self):
        response = self.client().post("/questions", json=self.new_question)
        body = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(body['success'], True)
        self.assertTrue(body['created'])

    def test_400_if_question_creation_not_allowed(self):

        response = self.client().post("/questions", content_type="application/json")
        self.assertEqual(response.status_code, 400)
        body = json.loads(response.data)
        self.assertEqual(body["message"], "Bad request")

    def test_play_quiz(self):
        new_quiz = {'previous_questions': [],
                    'quiz_category': {'type': 'Sports', 'id': 5}}

        res = self.client().post('/quizzes', json=new_quiz)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

    def test_422_play_quiz(self):
        new_quiz_round = {'previous_questions': []}
        res = self.client().post('/quizzes', json=new_quiz_round)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable entity")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
