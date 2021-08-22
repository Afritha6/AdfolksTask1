import unittest
import requests


class TestAPI(unittest.TestCase):
    URL = "http://127.0.0.1:5000/topic"

    data = {
        "commment": "AWS is a public cloud provider",
        "id": 3,
        "topic_name": "AWS"
    }


    def test_1_get_all_topics(self):
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code,200)
        self.assertEqual(len(resp.json()) ,len(resp.json()))
        print("Test 1 completed")

    

    def test_2_post_topic(self):
        resp = requests.post(self.URL,json=self.data)
        self.assertEqual(resp.status_code,200)
        print("Test 2 completed")


if __name__=="__main__":
    tester = TestAPI()

    tester.test_1_get_all_topics()
    tester.test_2_post_topic()

