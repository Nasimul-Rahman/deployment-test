from django.urls import path
#now import the views.py file into this code
from .views import index
urlpatterns=[
  path('', index)
]
