from django.urls import path
from . import views
urlpatterns = [
    path('', views.homePage,name='homePage'),
    path('sharePage', views.sharePage,name='sharePage'),
    path('instructions', views.Instructions,name='Instructions'),

]