from django.shortcuts import render,redirect
from main import models
from django.views.generic import TemplateView,ListView,DetailView,CreateView
from django.http import HttpResponseRedirect
from main.forms import PaymentForm,StoryForm,FeaturedForm,PDFform
from django.contrib.auth.decorators import login_required


class Index(TemplateView):
    template_name = 'main/index.html'

class Genre(ListView):
    model = models.Genre
    template_name = 'main/genre.html'

class Stories(ListView):
    model = models.Story
    template_name = 'main/stories.html'

@login_required
def Stories(request , pk):
    stories = models.Story.objects.filter(genre = pk )

    try:
        is_producer = models.ProducerProfile.objects.get(producer = request.user)
    except:
        is_producer = None

    context = {
        'user' : is_producer,
        'stories' : stories
    }

    return render(request,'main/stories.html',context)

class Story(DetailView):
    model = models.Story
    template_name = 'main/story.html'

@login_required
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
            story.producer = payment.producer
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

@login_required
def MyProfile(request):
    is_producer = None
    is_writer = None
    feautured_stories = models.Story.objects.filter(is_featured = True)

    try:
        is_producer = models.ProducerProfile.objects.get(producer = request.user)
    except:
        is_writer = models.WriterProfile.objects.get(writer = request.user)

    if is_producer is not None :
        featured = feautured_stories.filter(producer = is_producer)
        deals = models.Payment.objects.filter(producer = is_producer)
        context={
            'profile' : is_producer,
            'user' : is_producer.producer,
            'stories': None,
            'featured' : featured,
            'deals' : deals,
        }
    else :
        featured = feautured_stories.filter(writer = is_writer)
        context = {
            'profile' : is_writer,
            'user' : is_writer.writer,
            'stories' : is_writer.story_set.all(),
            'featured' : featured,
            'deals' : None
            
        }
    return render(request,'main/my_profile.html',context)

@login_required
def ViewWriterProfile(request , pk):
    
    try:
        is_producer = models.ProducerProfile.objects.get(producer = request.user)
    except:
        is_producer = None

    writer= models.WriterProfile.objects.get(pk = pk)
    featured = models.Story.objects.filter(writer = writer).filter(is_featured = True)
    unsold = models.Story.objects.filter(writer = writer).filter(is_featured= False).filter(is_sold = False)
    context = {
        'writer' : writer,
        'featured' : featured,
        'stories' : unsold,
        'user' : is_producer,
    }
    return render(request,'main/writer_profile.html',context)

@login_required
def ViewProducerProfile(request , pk):
    producer = models.ProducerProfile.objects.get(id = pk)
    featured = models.Story.objects.filter(producer = producer).filter(is_featured = True)
    context = {
        'producer' : producer,
        'featured' : featured,
    }
    return render(request,'main/producer_profile.html',context)
    

class FeaturedStories(ListView):
    queryset = models.Story.objects.filter(is_featured = True)
    template_name = 'main/index.html'
    context_object_name = 'featured'

@login_required
def story_upload(request):
    
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)

        if form.is_valid():
            story = form.save(commit=False)
            story.writer = models.WriterProfile.objects.get(writer = request.user)
            story.save()
            form.save_m2m()
            return redirect('my_profile')
    else:
        form = StoryForm()

    return render(request, 'main/story_upload.html', {
        'form': form,
    })

@login_required
def featured_upload(request,pk):
    story = models.Story.objects.get(pk = pk)
    if request.method == 'POST':
        form = FeaturedForm(request.POST, request.FILES)

        if form.is_valid():
            featured = form.save(commit = False)
            featured.story = story
            featured.save()
            story.is_featured = True
            story.save()
            return redirect('my_profile')
    else:
        form = FeaturedForm()

    return render(request, 'main/featured_upload.html', {
        'form': form,
    })

@login_required
def Add_PDF(request,pk):
    story = models.Story.objects.get(pk = pk)
    if request.method == 'POST':
        form = PDFform(request.POST, request.FILES, instance= story)

        if form.is_valid():
            form.save()

            return redirect('my_profile')
    else:
        form = PDFform()

    return render(request, 'main/pdf_upload.html', {
        'form': form,
    })