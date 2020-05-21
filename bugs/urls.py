from django.urls import path, include
from bugs.views import home

urlpatterns = [
    path('', home, name='home')
]
