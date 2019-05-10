from django.urls import path

from . import views

app_name = 'mock'
urlpatterns = [
    path('test', views.test, name='test'),
    path('', views.index, name='index')
]
