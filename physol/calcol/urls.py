from django.urls import path
from . import views

urlpatterns = [ 
    path('scalc', views.scalc, name=''), 
    path('',views.index, name='index')
]
