from django.urls import path
from . import views

urlpatterns = [ 
    path('scalc', views.scalc, name='scienece calculation'),
    path('ncalc', views.ncalc, name='neutron calculation'), 
    path('',views.index, name='index')
]
