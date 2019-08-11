from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from main import models

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(max_length = 256)
    last_name = forms.CharField(max_length= 256)

    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password1', 'password2')

    def save(self, commit = True):
        user= super().save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

    
        if commit:
            user.save()
        return user

class WriterProfileForm(forms.ModelForm):
    class Meta:
        model = models.WriterProfile
        fields = ['workex','bio','contact']
        

class ProducerProfileForm(forms.ModelForm):
    class Meta:
        model = models.ProducerProfile
        fields = ['workex','bio','contact','company']
