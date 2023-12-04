from django.urls import path
from . import views

app_name = "entidades"

urlpatterns = [
    path('', views.index, name="index"),
    path('trabxarea/<int:fid>/', views.trabxarea, name="trabxarea"),
    path('trabs/', views.trabs, name="trabs"),

    path('addA/<int:fid>/', views.addA, name="addA"),
    path('addT/<int:fid>/', views.addT, name="addT"),

    path('updA/<int:fid>/', views.updA, name="updA"),
    path('updT/<int:fid>/', views.updT, name="updT"),

    path('dele/<int:id>/<int:ent>/', views.dele, name="dele"),
    path('setHead/<int:id>/<int:opt>/', views.setHead, name="setHead"),
]