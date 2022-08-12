import os
from flask import (Flask, request, abort, jsonify)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    '''
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    '''

    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
    # CORS(app)

    '''
    @TODO: Use the after_request decorator to set Access-Control-Allow
    '''
    # defining CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true'
        )
        response.headers.add(
            'Access-Control-Allow-Methods',
            'DELETE, POST, GET, PATCH, PUT, OPTIONS'
        )
        return response

    # paginating question into pages with ten question per page
    def paginate_questions(req, selection):
        page = req.args.get('page', 1, type=int)
        start = (page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE
        questions = [question.format() for question in selection]
        return questions[start:end]

    '''
  @TODO:
  Create an endpoint to handle GET requests
  for all available categories.
  '''
    # Done
    # handle GET requests for all available categories.
    @app.route('/categories', methods=['GET'])
    def get_categories():
        query = Category.query.all()
        return jsonify({
            'status_code': 200,
            'categories': {c.id: c.type for c in query}
        })

    '''
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    '''
    @app.route('/questions', methods=['GET'])
    def get_questions():
        categories = Category.query.order_by(Category.id).all()
        query = Question.query.order_by(Question.id).all()
        questions = paginate_questions(request, query)

        if len(questions) == 0:
            abort(404)

        return jsonify({
            "success": True,
            "total_questions": len(questions),
            "questions": questions,
            "categories": {c.id: c.type for c in categories},
            "current_category": None
        })

    '''
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    '''
    # Done
    # DELETE question using a question ID.
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            # the query gets a queestion base on id and if not found it
            # triggers 404 error
            del_question = Question.query.get_or_404(question_id)
            del_question.delete()
            query = Question.query.all()
            questions = paginate_questions(request, query)
            return jsonify({'success': True,
                            'deleted': question_id,
                            'message': 'post deleted',
                            'questions': questions}
                           )
        except BaseException:
            abort(404)

    '''
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    '''
    # done
    # A post end point to create question
    @app.route('/questions', methods=['POST'])
    def create_question():

        body = request.get_json()
        if not body:
            abort(400)

        question = Question(
            question=body.get('question'),
            answer=body.get('answer'),
            category=body.get('category'),
            difficulty=body.get('difficulty')
        )
        try:
            question.insert()
            return jsonify({
                'success': True,
                'status_code': 200,
                'created': question.id
            })
        except BaseException:
            question.rollback()
            abort(422)
        finally:
            question.close_db()

    '''
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    '''
    # Done
    # A POST endpoint to get questions based on a search term
    @app.route('/questions/search', methods=['POST'])
    def search_question():
        body = request.get_json()
        if body is None or "searchTerm" not in body:
            abort(404)

        try:
            search_query = body.get("searchTerm", None)
            selection = Question.query.filter(
                Question.question.ilike(f"%{search_query}%")
            ).all()
            questions = paginate_questions(request, selection)

            return jsonify({
                'success': True,
                'questions': questions,
                'current_category': None,
                'total_questions': len(questions)
            })
        except BaseException:
            abort(404)
        finally:
            Question.close_db()

    '''
    @TODO:
    Create a GET endpoint to get questions based on category.
    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    '''
    # Done
    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def get_question_by_category(category_id):
        try:
            selection = Question.query.filter_by(category=category_id).all()
            questions = paginate_questions(request, selection)

            return jsonify({
                'success': True,
                'questions': questions,
                'total_questions': len(questions),
                'current_category': category_id
            })
        except BaseException:
            abort(422)

    '''
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    '''

    @app.route('/quizzes', methods=['POST'])
    def get_quiz_to_play():
        body = request.get_json()

        try:
            prev_questions = []
            quiz_category = []

            # case category and previous questions does not exits
            if (body.get('quiz_category')['id'] == 0):
                questions = Question.query.all()

            # case category and previous questions exits
            elif ('quiz_category' and 'previous_questions') in body:
                quiz_category = body.get('quiz_category')
                prev_questions = body.get('previous_questions')

                questions = Question.query.filter(
                    Question.category == quiz_category['id']
                ).filter(Question.id.notin_(prev_questions)).all()

            # case category alone exits
            elif 'quiz_category' in body:
                questions = Question.query.filter_by(
                    category=body.get("quiz_category"))

            next_question = questions[random.randint(
                0, len(questions))].format() if len(questions) != 0 else None
            return jsonify({"question": next_question})
        except BaseException:
            abort(422)

    '''
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    '''
    @app.errorhandler(400)
    def handle_400_bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad request"
        }), 400

    @app.errorhandler(404)
    def handle_404_not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Page not found"
        }), 404

    @app.errorhandler(405)
    def handle_405_invalid_method(error):
        return jsonify({
            "success": False,
            'error': 405,
            "message": "Invalid method!"
        }), 405

    @app.errorhandler(422)
    def handle_422_unprocessable_entity(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable entity"
        }), 422

    @app.errorhandler(500)
    def handle_500_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "server error"
        }), 500

    return app