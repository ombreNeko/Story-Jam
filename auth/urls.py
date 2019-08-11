from auth import views
from django.urls import path

urlpatterns = [
    path('login/',views.Login.as_view(), name= "login"),
    path('logout/',views.Logout.as_view(), name="logout"),
    path('writer_signup/', views.Writer_Signup, name = 'writer_signup'),
    path('producer_signup/', views.Producer_Signup, name = 'producer_signup'),

]