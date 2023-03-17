from django.urls import path
from srh.views import *
app_name='srh'

urlpatterns=[
    path('bhuvi/', bhuvi, name='bhuvi'),
    path('venky/', venky, name='venky'),

]





