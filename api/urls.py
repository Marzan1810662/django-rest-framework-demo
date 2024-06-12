from home.views import index,person,persondetails
from book.views import BookView
from django.urls import path

urlpatterns = [
    path('index/', index),
    path('person/', person),
    path('person/<int:pk>', persondetails),
    path('books/', BookView.as_view(), name='book-list-create')
]
