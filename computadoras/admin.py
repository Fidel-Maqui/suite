from django.contrib import admin
from computadoras import models
# Register your models here.
# @admin.register(models.Marcas)
# class MarcaAdmin(admin.ModelAdmin):
#     search_fields = ('nombre',)
#     ordering = ('nombre',)
# admin.site.register(models.Computadora)
@admin.register(models.Computadora)
class ComputadoraAdmin(admin.ModelAdmin):
    search_fields = ( 'responsable', 'nombre', 'ip',)
    list_display = ('responsable', 'nombre', 'ip',)#colmunas q se ven en la tabla
    ordering = ('nombre',)
    list_filter = ('responsable',  'nombre', 'ip',)#sidebar para filtrar
admin.site.register(models.Hardware)
admin.site.register(models.Periferico)
admin.site.register(models.Diferencias)
admin.site.register(models.Programs)
@admin.register(models.Softwares)
class SoftwaresAdmin(admin.ModelAdmin):
    search_fields = ( 'nombre',)
    ordering = ('nombre',)
    list_filter = ('nombre',)
    # list_display = ('nombre',)#colmunas q se ven en la tabla

