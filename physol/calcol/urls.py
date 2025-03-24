from django.urls import path
from . import views

urlpatterns = [ path('scalc', views.scalc, name=''), ]
