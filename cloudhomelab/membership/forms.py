from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models

from pyexpat import model
from django import forms
from membership.models import Textiles

class TextilesForm(forms.ModelForm):
    class Meta:
        model = Textiles
        fields = "__all__"


class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


