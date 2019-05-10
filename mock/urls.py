from django.urls import path

from . import views
"""
set unfinished path's default as index
"""
app_name = 'mock'
urlpatterns = [
    path('test', views.test, name='test'),
    path('search', views.index, name='search'),
    path('latest_reviews', views.latest_reviews, name='latest_reviews'),
    path('follow_reviews', views.index, name='follow_reviews'),
    path('course', views.index, name='course_index'),
    path('course/popular', views.index, name='course_popular'),
    path('course/public', views.index, name='course_public'),
    path('', views.index, name='index'),
]
