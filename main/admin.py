from django.contrib import admin
from main import models
admin.site.register ([
    models.WriterProfile,
    models.ProducerProfile,
    models.Story,
    models.Genre,
    models.Payment
])
