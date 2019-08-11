from django.shortcuts import render
from main import models
from django.views.generic import TemplateView,ListView,DetailView,CreateView
from django.http import HttpResponseRedirect

class Index(TemplateView):
    template_name = 'main/index.html'