from django.test import TestCase
from django.contrib.auth.models import User
from accounts.forms import RegistrationForm, ProfileEditForm, ClubForm, ClubEditForm


class TestForms(TestCase):
    def test_registration(self):
        #form_data = {'first_name': 'First', 'last_name': 'Last', 'email': 'Email@innopolis.ru'}
        form_data = {'username': 'username', 'first_name': 'username', 'last_name': 'username',
                     'email': 'username@innopolis.ru', 'password1': '123qwe[]', 'password2': '123qwe[]'}

        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_edit_profile(self):
        #form_data = {'first_name': 'First', 'last_name': 'Last', 'email': 'Email'}
        form_data = {'first_name': 'First', 'last_name': 'Last', 'email': 'Email@innopolis.ru'}

        form = ProfileEditForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_create_club(self):
        User.objects.create_user('foo', 'myemail@test.com', 'bar')
        user = User.objects.get(username="foo")
        form_data = {'leader': user.pk, 'club_name': 'Test_Club', 'club_description': 'description', 'club_schedule': 'schedule'}
        #form_data = {'type': 'Type', 'description': 'description'}
        form = ClubForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_edit_club(self):
        User.objects.create_user('foo', 'myemail@test.com', 'bar')
        user = User.objects.get(username="foo")
        form_data = {'leader': user.pk, 'club_name': 'Test_Club', 'club_description': 'description',
                     'club_schedule': 'schedule'}
        #form_data = {'type': 'Type', 'description': 'description'}
        form = ClubEditForm(data=form_data)
        self.assertTrue(form.is_valid())