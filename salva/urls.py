from django.urls import path
from salva import views
app_name = "salva"

urlpatterns = [
    path('', views.index, name="index"),
    path('save_area/', views.save_area, name="save_area"),
    path('save_trabs/', views.save_trabs, name="save_trabs"),
    path('save_comp/', views.save_comp, name="save_comp"),
    path('save_hard/', views.save_hard, name="save_hard"),
    path('save_peri/', views.save_peri, name="save_peri"),
    path('save_dife/', views.save_dife, name="save_dife"),
    path('save_prog/', views.save_prog, name="save_prog"),
    path('save_soft/', views.save_soft, name="save_soft"),

    path('rest_area/', views.rest_area, name="rest_area"),
    path('rest_trabs/', views.rest_trabs, name="rest_trabs"),
    path('rest_comp/', views.rest_comp, name="rest_comp"),
    path('rest_hard/', views.rest_hard, name="rest_hard"),
    path('rest_peri/', views.rest_peri, name="rest_peri"),
    path('rest_dife/', views.rest_dife, name="rest_dife"),
    path('rest_prog/', views.rest_prog, name="rest_prog"),
    path('rest_soft/', views.rest_soft, name="rest_soft"),

]
