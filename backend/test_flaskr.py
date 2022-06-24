import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres', 'ibuchi596643', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {"question": "How are you?", "answer": "I am fine",
         "difficulty": "1", "category": "2"}


        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    # 200 Success Test
    def test_get_categories(self):
        res = self.client().get("/categories")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["categories"])
    

    #---------------------------------- Pagination ----------------------------------------#
    # 200 Success Test
    def test_get_paginated_questions(self):
        res = self.client().get("/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])
        self.assertTrue(data["currentCategory"])
        self.assertTrue(data["categories"])
        self.assertTrue(len(data["questions"]))

    # 404 Error Test
    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get("/questions?page=5000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")


    #---------------------------------- Delete Question ----------------------------------------#
    # Success Test
    # def test_delete_question(self):
    #     res = self.client().delete("/questions/16")
    #     data = json.loads(res.data)

    #     question = Question.query.filter(Question.id == 16).one_or_none()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)
    #     self.assertEqual(data["deleted"], 16)
    #     self.assertEqual(question, None)

    # 422 Error Test
    def test_422_if_question_does_not_exist(self):
        res = self.client().delete("/questions/500")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")


    #---------------------------------- Create New Question ----------------------------------------#
    # 200 Success Test
    def test_create_new_question(self):
        res = self.client().post("/questions", json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["new_question"])
        self.assertTrue(len(data["questions"]))

    # 405 Error Test
    def test_405_if_question_creation_not_allowed(self):
        res = self.client().post("/questions/50", json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "method not allowed")


    #---------------------------------- Question Search ----------------------------------------#
    # 200 Success Test
    def test_for_question_search(self):
        res = self.client().post("/questions/search", json = { "searchTerm": "the"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])

    # 404 Error Test
    def test_404_sent_no_question_found(self):
        res = self.client().post("/questions/search", json = { "searchTerm": 500})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")


    #---------------------------------- Question Based on Category ------------------------------------#
    # 200 Success Test
    def test_get_question_based_on_category(self):
        res = self.client().get("/categories/3/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])
        self.assertTrue(data["totalQuestions"])

    # 405 Error Test 
    def test_405_if_request_category_does_not_exist(self):
        res = self.client().get("/categories/200/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()