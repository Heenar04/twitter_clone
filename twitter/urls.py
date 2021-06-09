from django.urls import path

from . import views

urlpatterns = [
    path('',views.Tweet,name='Tweet'),
    # path('',views.T,name='index'),

]