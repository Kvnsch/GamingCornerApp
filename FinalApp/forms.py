from django import forms
from FinalApp.models import upcomingGame
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2=forms.CharField(label="Reingrese Contraseña",widget=forms.PasswordInput)
    class Meta: 
        model = User
        fields = ['username','email','password1','password2']


class GameForm(forms.Form):
    gameDeveloper=forms.CharField(max_length=50)
    gameName=forms.CharField(max_length=70)
    gameGenre=forms.CharField(max_length=30)
    gameRelease=forms.DateField()
    gameScore=forms.FloatField()
    gameReview=forms.CharField(widget=forms.Textarea)

class UpcomingGameForm(forms.ModelForm):
    class Meta:
        model = upcomingGame
        fields = ['upcomingName','upcomingRelease','upcomingsWallpaper']