from django.urls import path
from . import views
app_name="reparaciones"

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add"),
    path('reparar/<int:id>/', views.reparar, name="reparar"),
    path('upd/<int:id>/', views.upd, name="upd"),
    path('dele/<int:id>/', views.dele, name="dele"),
]
