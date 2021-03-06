from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from home.models import Property

class SignUpForm(UserCreationForm):
   
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address.*')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' )

class PropertyForm(ModelForm):
    
    class Meta:
        model = Property
        fields=('institute_name','address','rent','conditioning','furnishing','rooms','occupancy','distance','phone','description','image')



