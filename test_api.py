import unittest
import ya_api


class TestYaApi(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def test_success_create_folder(self):
        self.assertEqual(ya_api.create_folder('test'), 201)
        print('test 1')

    def test_passed_create_folder(self):
        self.assertEqual(ya_api.create_folder('test_passed'), 409)
        print('test 2')

    def tearDown(self):
        # Удаляем папку после прохождения теста на создание папки
        ya_api.delete_folder('test')
        print('method tearDown')


if __name__ == '__main__':
    unittest.main()