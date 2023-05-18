from django.urls import path
from App_Stream import views

app_name = 'App_Stream'

urlpatterns = [

 path('', views.Home.as_view(), name='home'),
 path('comments/<int:video_id>/', views.comments, name='comments'),

]
