from django.urls import path

from . import views

urlpatterns = [
    path('', views.searchAPIView.as_view()),
   
]