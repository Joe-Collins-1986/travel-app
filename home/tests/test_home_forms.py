from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from home.forms import UserRegisterForm


class TestUserRegisterForm(TestCase):
    """ Test sign up form """

    def test_registration_form_valid(self):
        """ Registration form is valid """
        form = UserRegisterForm(data={
            'username': 'JoeBloggs',
            'email': 'JoeBloggs@test.com',
            'password1': 'Abc123456!',
            'password2': 'Abc123456!'
        })
        self.assertTrue(form.is_valid())

    def test_registration_invalid_passwords_dont_match(self):
        """ Registration form when passwords do not match """
        form = UserRegisterForm(data={
            'username': 'JoeBloggs',
            'email': 'JoeBloggs@test.com',
            'password1': 'Abc123456!',
            'password2': 'IncorrectPassword'
        })
        self.assertFalse(form.is_valid())

    def test_registration_invalid_passwords_no_special_characters(self):
        """ Registration form when passwords match but are not valid (e.g. no special characters) """
        form = UserRegisterForm(data={
            'username': 'JoeBloggs',
            'email': 'JoeBloggs@test.com',
            'password1': 'Abc123456',
            'password2': 'Abc123456'
        })
        self.assertFalse(form.is_valid())
    
    def test_registration_form_email_not_valid(self):
        """ Registration form when email not valid """
        form = UserRegisterForm(data={
            'username': 'JoeBloggs',
            'email': 'JoeBloggstest.com',
            'password1': 'Abc123456!',
            'password2': 'Abc123456!'
        })
        self.assertFalse(form.is_valid())


# CREATE TESTS DUPLICATING ACCOUNT INFO OF EXISSTING ACCOUNT

class SetupUserRegister(TestCase):
    """ Setup register """

    def setUp(self):
        self.user = User.objects.create(
            username="JoeBloggs",
            email="JoeBloggs@test.com",
            password="Abc123456!"
        )


class RegistrationFormDuplicateInfo(SetupUserRegister):
    """ Test if any field from register is duplicated """

    def test_duplicated_username_on_registration_form(self):
        """ Test if username is duplicated """
        form = UserRegisterForm(data={
            "username": "JoeBloggs",
        })
        self.assertFalse(form.is_valid())
        self.assertRaises(ValidationError)

    def test_duplicated_email_on_registration_form(self):
        """ Test if username is duplicated """
        form = UserRegisterForm(data={
            "email": "JoeBloggs@test.com",
        })
        self.assertFalse(form.is_valid())
        self.assertRaises(ValidationError)