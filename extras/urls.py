from django.urls import path
from . import views

app_name = "extras"

urlpatterns = [
path("banco_de_problemas/", views.banco, name="banco"),
path("banco_de_problemas/addProblema/", views.addProblema, name="addProblema"),
path("banco_de_problemas/updProblema/<int:id>/", views.updProblema, name="updProblema"),
path("banco_de_problemas/delProblema/<int:id>/", views.delProblema, name="delProblema"),

path("bajas/", views.bajas, name="bajas"),
path("bajas/darBaja_Comp/<int:id>/", views.darBaja_Comp, name="darBaja_Comp"),
path("bajas/darBaja_Hard/<int:id>/", views.darBaja_Hard, name="darBaja_Hard"),
path("bajas/darBaja_Peri/<int:id>/", views.darBaja_Peri, name="darBaja_Peri"),
]