from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.homePage,name='homePage'),
    path('sharePage', views.sharePage,name='sharePage'),
    path('instructions', views.Instructions,name='Instructions'),
    path('watermark/', include('waterMarker.urls')),

]