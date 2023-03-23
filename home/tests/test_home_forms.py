from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from home.forms import UserRegisterForm


class TestUserRegisterForm(TestCase):

    def test_registration_form_valid(self):
        form = UserRegisterForm(data={
            'username': 'JoeBloggs',
            'email': 'JoeBloggs@test.com',
            'password1': 'Abc123456!',
            'password2': 'Abc123456!'
        })
        self.assertTrue(form.is_valid())

    def test_registration_invalid_passwords_dont_match(self):
        form = UserRegisterForm(data={
            'username': 'JoeBloggs',
            'email': 'JoeBloggs@test.com',
            'password1': 'Abc123456!',
            'password2': 'IncorrectPassword'
        })
        self.assertFalse(form.is_valid())

    def test_registration_invalid_passwords_no_special_characters(self):
        form = UserRegisterForm(data={
            'username': 'JoeBloggs',
            'email': 'JoeBloggs@test.com',
            'password1': 'Abc123456',
            'password2': 'Abc123456'
        })
        self.assertFalse(form.is_valid())

    def test_registration_form_email_not_valid(self):
        form = UserRegisterForm(data={
            'username': 'JoeBloggs',
            'email': 'JoeBloggstest.com',
            'password1': 'Abc123456!',
            'password2': 'Abc123456!'
        })
        self.assertFalse(form.is_valid())


class SetupUserRegister(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username="JoeBloggs",
            email="JoeBloggs@test.com",
            password="Abc123456!"
        )


class RegistrationFormDuplicateInfo(SetupUserRegister):

    def test_duplicated_username_on_registration_form(self):
        form = UserRegisterForm(data={
            "username": "JoeBloggs",
        })
        self.assertFalse(form.is_valid())
        self.assertRaises(ValidationError)

    def test_duplicated_email_on_registration_form(self):
        form = UserRegisterForm(data={
            "email": "JoeBloggs@test.com",
        })
        self.assertFalse(form.is_valid())
        self.assertRaises(ValidationError)
