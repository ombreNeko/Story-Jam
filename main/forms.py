from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from main import models

class PaymentForm(forms.ModelForm):
    class Meta:
        model = models.Payment
        fields = ['mode','card_number','card_cvv','card_exp','name_on_card']
        