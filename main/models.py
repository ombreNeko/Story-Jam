
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