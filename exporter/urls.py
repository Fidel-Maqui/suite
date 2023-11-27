from django.urls import path
from . import views

app_name = "exporter"

urlpatterns = [
    path('topdf/<int:id>/',views.apdf_htmltopdf, name='topdf'),
    path('topdfview/<int:id>/',views.apdf_topdf, name='topdfview'),
]
