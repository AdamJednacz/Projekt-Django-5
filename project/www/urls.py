from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shoecreator/',views.shoe , name='shoe'),
    path('store/<int:store_id>/', views.store_detail, name='store_detail'),
   

]