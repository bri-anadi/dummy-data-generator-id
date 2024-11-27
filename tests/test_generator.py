import unittest
from datetime import datetime, timedelta
from dummy_data_generator import DummyDataGenerator


class TestDummyDataGenerator(unittest.TestCase):
    def test_generate_name(self):
        name = DummyDataGenerator.generate_name()
        self.assertTrue(name)
        self.assertIsInstance(name, str)

    def test_generate_email(self):
        email = DummyDataGenerator.generate_email()
        self.assertTrue('@' in email)
        self.assertTrue('.' in email.split('@')[1])

    def test_generate_phone(self):
        phone = DummyDataGenerator.generate_phone()
        self.assertTrue(phone.startswith('62'))
        self.assertEqual(len(phone), 11 or 12)

    def test_generate_address(self):
        address = DummyDataGenerator.generate_address()
        self.assertIn('street', address)
        self.assertIn('city', address)
        self.assertIn('province', address)
        self.assertIn('postal_code', address)

    def test_generate_birthdate(self):
        birthdate = DummyDataGenerator.generate_birthdate()
        self.assertIsInstance(birthdate, datetime)
        self.assertTrue((datetime.now() - birthdate).days > 365 * 18)
        self.assertTrue((datetime.now() - birthdate).days < 365 * 65)

    def test_generate_user_data(self):
        user = DummyDataGenerator.generate_user_data()
        self.assertIn('id', user)
        self.assertIn('name', user)
        self.assertIn('email', user)
        self.assertIn('username', user)
        self.assertIn('gender', user)
        self.assertIn('phone', user)
        self.assertIn('birthdate', user)
        self.assertIn('address', user)
        self.assertIn('job', user)
        self.assertIn('company', user)
        self.assertIn('credit_card', user)


if __name__ == '__main__':
    unittest.main()
