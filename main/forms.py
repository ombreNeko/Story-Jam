from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from main import models

class PaymentForm(forms.ModelForm):
    class Meta:
        model = models.Payment
        fields = ['mode','card_number','card_cvv','card_exp','name_on_card']


class StoryForm(forms.ModelForm):
    class Meta:
        model = models.Story
        fields = ('name', 'summary','genre', 'price','upload')

class FeaturedForm(forms.ModelForm):
        class Meta:
            model = models.Featured
            fields = ('name','duration','featuring_type','upload_vid','upload_img')

class PDFform(forms.ModelForm):
    class Meta:
        model = models.Story
        fields = ('upload',)


class UpdatePhotoFormWriter(forms.ModelForm):
    class Meta:
        model = models.WriterProfile
        fields = ('photo',)

class UpdatePhotoFormProducer(forms.ModelForm):
    class Meta:
        model = models.ProducerProfile
        fields = ('photo',)