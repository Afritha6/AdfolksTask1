import unittest
import requests


class TestAPI(unittest.TestCase):
    URL = "http://127.0.0.1:5000/topic"

    data = {'commment': None, 'id': 9, 'topic_name': 'dummydata2'}

    expected_result =  {'commment': None, 'id': 9, 'topic_name': 'dummydata2'}


    def test_1_get_all_topics(self):
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code,200)
        self.assertEqual(len(resp.json()) ,len(resp.json()))
        print("Test 1 completed")

    

    def test_2_post_topic(self):
        resp = requests.post(self.URL,json=self.data)
        self.assertEqual(resp.status_code,200)
        print("Test 2 completed")

    def test_3_get_specific_topic(self):
        resp = requests.get(self.URL + '/9')
        self.assertEqual(resp.status_code,200)
        self.assertDictEqual(resp.json() , self.expected_result)
        print("Test 3 completed")


if __name__=="__main__":
    tester = TestAPI()

    tester.test_1_get_all_topics()
    tester.test_2_post_topic()
    tester.test_3_get_specific_topic()

