from django.urls import path
from . import views
app_name="computadoras"

urlpatterns = [
    path('', views.index, name="index"),
    path('detalles/<int:id>/', views.detalles, name="detalles"),

    path('upd_comp/<int:id>/', views.upd_comp, name="upd_comp"),
    path('delc/<int:id>/<int:ent>/', views.delc, name="delc"),
    path('ping/<str:ip>/', views.ping, name="ping"),
    # path('ping/', views.ping, name="ping"),
    path('upd_hard/<int:id>/<int:c>/', views.upd_hard, name="upd_hard"),
    path('upd_peri/<int:id>/<int:c>/', views.upd_peri, name="upd_peri"),
    path('upd_prog/<int:id>/<int:c>/', views.upd_prog, name="upd_prog"),
    
    path('addC/<int:fid>/', views.addC, name="addC"),
    path('add_hard/<int:c>/', views.add_hard, name="add_hard"),
    path('add_peri/<int:c>/', views.add_peri, name="add_peri"),
    path('add_prog/<int:c>/', views.add_prog, name="add_prog"),

    
    path('verC/<int:fid>/', views.verC, name="verC"),
    path('verC_area/<int:fid>/', views.verC_area, name="verC_area"),

    path('del_all_difs/<int:comp>/', views.del_all_difs, name="del_all_difs"),
    path('del_dif/<int:id>/', views.del_dif, name="del_dif"),
    
    
    path('scan/', views.scan, name="scan"),
    path('programas/', views.programas, name="programas"),
    path('form_prog/', views.form_prog, name="form_prog"),
    path('scan_prog/', views.scan_prog, name="scan_prog"),
    path('upd_soft/<int:id>', views.upd_soft, name="upd_soft"),
]
