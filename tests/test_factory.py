import unittest

from utils.simple_factory import PhoneFactory, Phone, Samsung, AppleIPhone


class TestFactory(unittest.TestCase):
    def setUp(self):
        self.factory = PhoneFactory()


class TestIphone(TestFactory):
    def test_difference_id(self):
        self.assertFalse(
            self.factory.create_type('iphone') is self.factory.create_type(
                'iphone'))

    def test_is_a_phone(self):
        self.assertTrue(
            isinstance(self.factory.create_type('iphone'), Phone))
        self.assertTrue(
            isinstance(self.factory.create_type('iphone'), AppleIPhone))
        self.assertFalse(
            isinstance(self.factory.create_type('iphone'), Samsung))


if __name__ == '__main__':
    unittest.main()
