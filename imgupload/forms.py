from django import forms
from .models import Profile

class User_Form(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
                'fname',
                'lname',
                'technologies',
                'email',
                'display_picture'
                ]
