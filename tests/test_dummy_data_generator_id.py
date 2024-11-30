import unittest
from datetime import datetime
from dummy_data_generator_id.generator import DummyDataGeneratorId

class TestDummyDataGeneratorId(unittest.TestCase):
    def test_generate_name(self):
        # Test default random gender
        name = DummyDataGeneratorId.generate_name()
        self.assertIsInstance(name, str)
        self.assertTrue(len(name.split()) == 2)

        # Test male name
        male_name = DummyDataGeneratorId.generate_name('male')
        self.assertIsInstance(male_name, str)
        first_name = male_name.split()[0]
        self.assertTrue(first_name in [
            'Ahmad', 'Muhammad', 'Budi', 'Dedi', 'Rudi', 'Adi', 'Eko', 'Agus',
            'Hadi', 'Iwan', 'Bambang', 'Slamet', 'Hendro', 'Yulio', 'Taufik'
        ])

        # Test female name
        female_name = DummyDataGeneratorId.generate_name('female')
        self.assertIsInstance(female_name, str)
        first_name = female_name.split()[0]
        self.assertTrue(first_name in [
            'Siti', 'Ani', 'Dewi', 'Rina', 'Maya', 'Fitri', 'Indah', 'Rita',
            'Nurul', 'Rini', 'Lia', 'Susan', 'Erni', 'Wati', 'Yuni'
        ])

    def test_generate_email(self):
        # Test with provided name
        name = "John Doe"
        email = DummyDataGeneratorId.generate_email(name)
        self.assertIsInstance(email, str)
        self.assertTrue('@' in email)
        self.assertTrue(email.startswith('john.doe'))

        # Test without name
        random_email = DummyDataGeneratorId.generate_email()
        self.assertIsInstance(random_email, str)
        self.assertTrue('@' in random_email)

    def test_generate_phone(self):
        # Test default country code
        phone = DummyDataGeneratorId.generate_phone()
        self.assertIsInstance(phone, str)
        self.assertTrue(phone.startswith('62'))
        self.assertEqual(len(phone), 13)  # Including country code

        # Test custom country code
        custom_phone = DummyDataGeneratorId.generate_phone('1')
        self.assertTrue(custom_phone.startswith('1'))

    def test_generate_address(self):
        # Test random province
        address = DummyDataGeneratorId.generate_address()
        self.assertIsInstance(address, dict)
        self.assertTrue(all(key in address for key in ['street', 'city', 'province', 'postal_code']))

        # Test specific province
        specific_address = DummyDataGeneratorId.generate_address('DKI Jakarta')
        self.assertEqual(specific_address['province'], 'DKI Jakarta')

    def test_generate_job(self):
        job = DummyDataGeneratorId.generate_job()
        self.assertIsInstance(job, str)
        self.assertTrue(len(job.split(' - ')) == 2)

    def test_generate_company(self):
        company = DummyDataGeneratorId.generate_company()
        self.assertIsInstance(company, str)
        self.assertTrue(company.startswith(('PT', 'CV', 'Yayasan')))

    def test_generate_birthdate(self):
        birthdate = DummyDataGeneratorId.generate_birthdate()
        self.assertIsInstance(birthdate, datetime)

        # Test age range
        today = datetime.now()
        age = today.year - birthdate.year
        self.assertTrue(18 <= age <= 65)

        # Test custom age range
        young_birthdate = DummyDataGeneratorId.generate_birthdate(18, 25)
        age = today.year - young_birthdate.year
        self.assertTrue(18 <= age <= 25)

    def test_generate_credit_card(self):
        card = DummyDataGeneratorId.generate_credit_card()
        self.assertIsInstance(card, dict)
        self.assertTrue(all(key in card for key in ['type', 'number', 'expiry_date', 'cvv']))

        # Test Luhn algorithm
        number = card['number']
        self.assertTrue(DummyDataGeneratorId.luhn_checksum(number[:-1]) == int(number[-1]))

    def test_generate_random_word(self):
        word = DummyDataGeneratorId.generate_random_word()
        self.assertIsInstance(word, str)
        self.assertTrue(3 <= len(word) <= 10)
        self.assertTrue(word[0].isupper())
        self.assertTrue(word[1:].islower())

    def test_generate_uuid(self):
        uuid = DummyDataGeneratorId.generate_uuid()
        self.assertIsInstance(uuid, str)
        self.assertEqual(len(uuid), 36)  # Standard UUID length

    def test_generate_username(self):
        username = DummyDataGeneratorId.generate_username()
        self.assertIsInstance(username, str)
        # Check if ends with numbers
        self.assertTrue(any(c.isdigit() for c in username))

    def test_generate_user_data(self):
        # Test single user
        user = DummyDataGeneratorId.generate_user_data()
        self.assertIsInstance(user, dict)
        self.assertTrue(all(key in user for key in [
            'id', 'name', 'email', 'username', 'gender', 'phone',
            'birthdate', 'address', 'job', 'company', 'credit_card'
        ]))

        # Test multiple users
        users = DummyDataGeneratorId.generate_user_data(3)
        self.assertIsInstance(users, list)
        self.assertEqual(len(users), 3)
        self.assertTrue(all(isinstance(user, dict) for user in users))

if __name__ == '__main__':
    unittest.main()
