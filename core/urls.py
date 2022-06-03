from django.urls import path, include
from core import views 

# url pattern
urlpatterns = [
    path('', views.index, name = 'index'),
]