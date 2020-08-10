from django.urls import path
from weatherapp import views
app_name='weather'
urlpatterns=[
path('', views.index, name='index'),
path('about/',views.about,name='about'),
]
