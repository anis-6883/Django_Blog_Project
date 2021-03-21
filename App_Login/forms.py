from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email Address')
    class Meta:
        model  = User
        fields = ['username', 'email', 'password1', 'password2']


class UserProfileChangeForm(forms.ModelForm):
    email = forms.EmailField(label='Email Address')

    class Meta:
        model  = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ChangeProfilePicForm(forms.ModelForm):
    class Meta:
        model  = UserProfile
        fields = ['image']



# class UserProfileChangeForm(UserChangeForm):
#     password = None
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'first_name', 'last_name')


# class ChangeProfilePic(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['image']



