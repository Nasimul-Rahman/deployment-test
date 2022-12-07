from django.urls import path
#now import the views.py file into this code
from .views import index, about
urlpatterns=[
  path('', index, name='home'),
  path('about/', about, name='about')
]
