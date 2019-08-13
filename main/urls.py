from main import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.Index.as_view()), name = 'index'),
    path('genres/',login_required(views.Genre.as_view()), name = 'genres' ),
    path('genres/<int:pk>', views.Stories, name ='genre'),
    path('story/<int:pk>', views.Story.as_view(),name='story'),
    path('story/<int:pk>/payment', views.Payment, name = 'payment'),
    path('payment_successful/', views.Payment_Success.as_view() , name = 'success'),
    path('my_profile/', views.MyProfile , name = 'my_profile'),
    path('view_writer_profile/<int:pk>',views.ViewWriterProfile.as_view(),name = 'view_writer_profile'),
   ]