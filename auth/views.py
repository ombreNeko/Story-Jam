from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from .forms import ExtendedUserCreationForm,WriterProfileForm,ProducerProfileForm


def Writer_Signup(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        writer_profile_form = WriterProfileForm(request.POST)

        if form.is_valid() and writer_profile_form.is_valid():
            user = form.save()
            writer_profile = writer_profile_form.save(commit = False)
            writer_profile.writer = user
            writer_profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = 'username',password = 'password')
            
            login(request,user)
            return redirect('index')

    else:
        form = ExtendedUserCreationForm()
        writer_profile_form = WriterProfileForm()
        
    context = {
        'form' : form,
        'writer_profile_form' : writer_profile_form,
    }

    return render (request,'auth/writer_signup.html',context)


def Producer_Signup(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        producer_profile_form = ProducerProfileForm(request.POST)

        if form.is_valid() and producer_profile_form.is_valid():
            user = form.save()
            producer_profile = producer_profile_form.save(commit = False)
            producer_profile.producer = user
            producer_profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = 'username',password = 'password')
            
            login(request,user)
            return redirect('index')

    else:
        form = ExtendedUserCreationForm()
        producer_profile_form = ProducerProfileForm()
        
    context = {
        'form' : form,
        'producer_profile_form' : producer_profile_form,
    }

    return render (request,'auth/producer_signup.html',context)

