import unittest
import requests


class TestAPI(unittest.TestCase):
    URL = "http://127.0.0.1:5000/topic"


    def test_1_get_all_topics(self):
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code,200)
        self.assertEqual(len(resp.json()) ,len(resp.json()))
        print("Test 1 completed")

    

if __name__=="__main__":
    tester = TestAPI()

    tester.test_1_get_all_todos()

