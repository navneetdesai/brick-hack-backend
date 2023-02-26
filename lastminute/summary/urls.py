from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('lecture', views.lecture, name='lecture-features')
]