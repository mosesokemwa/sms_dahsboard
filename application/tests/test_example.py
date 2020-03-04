import unittest
from application.tests.test_base import BasicTests


class MyTestClass(BasicTests):

    def test_main_page(self):
        response = self.app.get('/main', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # test method
    def test_equal_numbers(self):
        self.assertEqual(2, 2)


# runs the unit tests in the module
if __name__ == '__main__':
    unittest.main()
