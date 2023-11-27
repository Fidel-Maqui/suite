from django.urls import path
from printers import views
app_name="printers"

urlpatterns = [
    path("", views.index, name="index"),

    path("add_conn/", views.add_conn, name="add_conn"),
    path("upd_conn/<int:id>/", views.upd_conn, name="upd_conn"),
    path("del_conn/<int:id>/", views.del_conn, name="del_conn"),
    
    path("add_printer/", views.add_printer, name="add_printer"),
    path("upd_printer/<int:id>/", views.upd_printer, name="upd_printer"),
    path("del_printer/<int:id>/", views.del_printer, name="del_printer"),
    path("list_printer/", views.list_printer, name="list_printer"),
]