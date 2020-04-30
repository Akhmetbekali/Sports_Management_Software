from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms

from accounts.models import ClubProfile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            students_group = Group.objects.get(name='student')
            students_group.user_set.add(user)


class ProfileEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = {
            'email',
            'first_name',
            'last_name',
            'password',
            'groups',
        }


class ClubForm(forms.ModelForm):
    class Meta:
        model = ClubProfile
        fields = (
            'leader',
            'club_name',
            'club_description',
            'club_schedule'
        )

    def save(self, commit=True):
        club = super(ClubForm, self).save(commit=False)
        club.leader = self.cleaned_data['leader']
        club.club_name = self.cleaned_data['club_name']
        club.club_description = self.cleaned_data['club_description']
        club.club_schedule = self.cleaned_data['club_schedule']
        if commit:
            club.save()


class ClubEditForm(forms.ModelForm):
    class Meta:
        model = ClubProfile
        fields = {
            'leader',
            'club_name',
            'club_description',
            'club_schedule'
        }
