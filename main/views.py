from django.shortcuts import render,redirect
from main import models
from django.views.generic import TemplateView,ListView,DetailView,CreateView
from django.http import HttpResponseRedirect
from main.forms import PaymentForm

class Index(TemplateView):
    template_name = 'main/index.html'

class Genre(ListView):
    model = models.Genre
    template_name = 'main/genre.html'

class Stories(DetailView):
    model = models.Genre
    template_name = 'main/stories.html'

def Stories(request , pk):
    genre = models.Genre.objects.get(pk = pk)

    try:
        is_producer = models.ProducerProfile.objects.get(producer = request.user)
    except:
        is_producer = None

    context = {
        'user' : is_producer,
        'genre' : genre
    }

    return render(request,'main/stories.html',context)

class Story(DetailView):
    model = models.Story
    template_name = 'main/story.html'
    
def Payment(request,pk):
    
    story = models.Story.objects.get(pk = pk )

    if request.method == 'POST':
        form = PaymentForm(request.POST)

        if form.is_valid():
            
            payment = form.save(commit = False)
            payment.producer = models.ProducerProfile.objects.get(producer = request.user)
            payment.story = story
            payment.save()
            story.is_sold = True
            story.save()

            return redirect('success')

    else:
        form = PaymentForm()
        
    context = {
        'form' : form,
        'story': story
    }

    return render (request,'main/payment.html',context)

class Payment_Success(TemplateView):
    template_name = 'main/payment_success.html'

def MyProfile(request):
    is_producer = None
    is_writer = None

    try:
        is_producer = models.ProducerProfile.objects.get(producer = request.user)
    except:
        is_writer = models.WriterProfile.objects.get(writer = request.user)

    if is_producer is not None :
        context={
            'profile' : is_producer,
            'user' : is_producer.producer,
            'stories': None
        }
    else :
        context = {
            'profile' : is_writer,
            'user' : is_writer.writer,
            'stories' : is_writer.story_set.all()
            
        }
    return render(request,'main/my_profile.html',context)

class ViewWriterProfile(DetailView):
    model = models.WriterProfile
    template_name = 'main/writer_profile.html'
    