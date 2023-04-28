
import email
from http.client import METHOD_NOT_ALLOWED
from django.db.models.fields import EmailField
from django.forms import ModelForm, fields
from django.forms.models import ModelForm
from .models import Blospost, Students
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class PostForm(ModelForm):
    class Meta:
        model = Blospost
        fields = ['title', 'content', 'tag', 'date_posted']


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = '__all__'


# id = models.BigAutoField(primary_key=True)
#     title = models.CharField(max_length=150)
#     content = models.CharField(max_length=2000)
#     tag = models.CharField(max_length=100)
#     date_posted = models.DateField(max_length=100)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
