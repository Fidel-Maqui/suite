from django.contrib import admin
from printers.models import PrinterOwner, PrinterStack
# Register your models here.
admin.site.register(PrinterOwner)
admin.site.register(PrinterStack)
