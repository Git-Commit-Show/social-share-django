from django.urls import path
from . import views
urlpatterns = [
    path('', views.sharePage,name='sharePage'),
]