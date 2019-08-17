from main import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.FeaturedStories.as_view()), name = 'index'),
    path('genres/',login_required(views.Genre.as_view()), name = 'genres' ),
    path('genres/<int:pk>', login_required(views.Stories), name ='genre'),
    path('story/<int:pk>', views.Story.as_view(),name='story'),
    path('story/<int:pk>/payment', views.Payment, name = 'payment'),
    path('payment_successful/', login_required(views.Payment_Success.as_view()) , name = 'success'),
    path('my_profile/', views.MyProfile , name = 'my_profile'),
    path('view_writer_profile/<int:pk>',views.ViewWriterProfile,name = 'view_writer_profile'),
    path('view_producer_profile/<int:pk>',views.ViewProducerProfile,name = 'view_producer_profile'),
    path('upload_story/',views.story_upload, name = 'story_upload'),
    path('story/<int:pk>/upload_featured',views.featured_upload, name = 'featured_upload'),
    path('story/<int:pk>/add_pdf',views.Add_PDF,name = 'add_pdf'),
    path('my_profile/<int:pk>/update_dp', views.UpdatePhoto, name= 'update_profile_pic'),
  
   ]