import unittest

from restapi import app, db


TEST_DB = 'test.db'


class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        # db.drop_all()
        db.create_all()

    
        self.assertEqual(app.debug, False)

    # executed after each test
    # def tearDown(self):
    #     pass


    ########################
    #### helper methods ####
    ########################

    def getalltopic(self):
        return self.app.get(
            '/topic'
            # data=dict(commment=commment, id=id, topic_name=topic_name),
            # follow_redirects=True
        )

    def post(self, commment, id, topic_name):
        return self.app.post(
            '/topic',
            data=dict(commment=commment, id=id, topic_name=topic_name),
            follow_redirects=True
        )

    def getspecifictopic(self):
        return self.app.get(
            '/topic/2'
            # data=dict(commment=commment, id=id, topic_name=topic_name),
            # follow_redirects=True
        )

    def updatetopic(self, commment, id, topic_name):
        return self.app.put(
            '/topic/2',
            data=dict(commment=commment, id=id, topic_name=topic_name),
            follow_redirects=True
        )
    
    def updatecomment(self, commment, id, topic_name):
        return self.app.put(
            '/topic/2/comment',
            data=dict(commment=commment, id=id, topic_name=topic_name),
            follow_redirects=True
        )

    ###############
    #### tests ####
    ###############

    def test_1_get_all_topics(self):
        resp = self.getalltopic()
        self.assertEqual(resp.status_code,200)
    
    def test_2_post_topic(self):
        resp = self.post(None,'2','dummydata1')
        self.assertEqual(resp.status_code,200)

    def test_3_get_specific_topic(self):
        resp = self.getspecifictopic()
        self.assertEqual(resp.status_code,200)

    def test_4_update(self):
        resp = self.updatetopic(None,'2','dummydata1updated')
        self.assertEqual(resp.status_code,200)

    def test_5_addcomment(self):
        resp = self.updatecomment('comment updated','2','dummydata1updated')
        self.assertEqual(resp.status_code,200)


if __name__ == "__main__":
    unittest.main()
