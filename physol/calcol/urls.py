from django.urls import path
from . import views

urlpatterns = [ 
    path('pcalc', views.pcalc, name='physics calculation'),
    path('mcalc', views.mcalc, name='mathmatics calculator'),
    path('ncalc', views.ncalc, name='neutron calculation'),
    path('pwg', views.pwg, name='password generator'), 
    path('',views.index, name='index')
]
