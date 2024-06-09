from home.views import index,person,persondetails
from django.urls import path

urlpatterns = [
    path('index/', index),
    path('person/', person),
    path('person/<int:pk>', persondetails),
]
