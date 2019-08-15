
from django.db import models
from django.contrib.auth.models import User

class WriterProfile(models.Model):
    writer = models.OneToOneField(User,on_delete = models.CASCADE)
    workex = models.PositiveIntegerField()
    bio = models.TextField(null= True, blank= True)
    photo = models.URLField(null = True, blank= True)
    contact = models.CharField(max_length = 12)
    def __str__(self):
        return self.writer.username

class ProducerProfile(models.Model):
    producer = models.OneToOneField(User,on_delete = models.CASCADE)
    workex = models.PositiveIntegerField()
    bio = models.TextField(null= True, blank= True)
    photo = models.URLField(null = True, blank= True)
    contact = models.CharField(max_length = 12)
    company  = models.CharField(max_length = 256)
    def __str__(self):
        return self.producer.username

class Story(models.Model):
    name = models.CharField(max_length = 256)
    price = models.FloatField()
    summary = models.TextField()
    is_sold = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    writer = models.ForeignKey(WriterProfile, on_delete = models.DO_NOTHING, null= True, blank = True)
    producer = models.ForeignKey(ProducerProfile,on_delete= models.DO_NOTHING, null = True, blank = True)
    upload = models.FileField(upload_to='upload_story/',null = True , blank = True)
    uploaded_at = models.DateTimeField(auto_now_add=True,null = True)
    genre = models.ManyToManyField('Genre')

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length = 256, default = 'fantasy')
    def __str__(self):
        return self.name


class Payment(models.Model):
    PAYMENT_OPTIONS = [
        ('cc', 'Credit Card'),
        ('dc', 'Debit Card'),
    ]
    producer = models.ForeignKey(ProducerProfile,on_delete= models.DO_NOTHING)
    story = models.ForeignKey('Story', on_delete = models.CASCADE)
    mode = models.CharField(max_length = 256, choices = PAYMENT_OPTIONS)
    payment_time = models.DateTimeField(auto_now_add = True)
    card_number = models.CharField(max_length = 256)
    card_cvv = models.CharField(max_length = 3)
    card_exp = models.CharField(max_length = 5)
    name_on_card = models.CharField(max_length = 256)

    def __str__(self):
        return "{} bought {} story".format(self.producer.producer.username, self.story.name)

class Featured(models.Model):
    FEATURING_TYPE = [
        (1,'Short-film-animated'),
        (2,'Short-film'),
        (3,'Animated movie'),
        (4,'Movie'),
    ]
    name = models.CharField(max_length = 256)
    duration = models.PositiveIntegerField()
    featuring_type = models.IntegerField(choices= FEATURING_TYPE)
    story = models.OneToOneField('Story', on_delete = models.DO_NOTHING,null = True)
    upload_vid = models.FileField(upload_to='upload_featured/',null = True , blank = True)
    upload_img = models.ImageField(upload_to = 'upload_img/',null = True, blank = True)
    def __str__(self):
        return self.name