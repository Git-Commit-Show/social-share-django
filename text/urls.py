from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.upload,name='upload'),
    path('download/',views.viewAll,name='viewAll')
]

