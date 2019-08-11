from auth import views
from django.urls import path

urlpatterns = [
    path('writer_signup/', views.Writer_Signup, name = 'writer_signup'),
    path('producer_signup/', views.Producer_Signup, name = 'producer_signup'),

]