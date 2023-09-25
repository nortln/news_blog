from django.contrib.auth.models import User

from django import forms
from .models import New, Comment

class RegisterationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]


class AddBlog(forms.ModelForm):
    class Meta:
        model = New
        fields = "__all__"


class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]