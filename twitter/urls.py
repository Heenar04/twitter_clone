from django.urls import path
from . import views


urlpatterns = [
    path('',views.Tweet,name='Tweet'),
    path('delete/<int:id>/',views.delete),
    path('contact/',views.Contacts, name='contacts'),
]
