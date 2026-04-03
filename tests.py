import unittest
from app import app

class TestTodoAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_list_empty(self):
        resp = self.client.get('/api/todos')
        self.assertEqual(resp.status_code, 200)

    def test_create_todo(self):
        resp = self.client.post('/api/todos', json={"title": "Buy milk"})
        self.assertEqual(resp.status_code, 201)

if __name__ == '__main__':
    unittest.main()
