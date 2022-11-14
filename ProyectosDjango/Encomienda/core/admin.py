from django.contrib import admin
from.models import residencia, correspondencia

# Register your models here.
#@admin.register(residencia)
#class residenciaAdmin(admin. ModelAdmin):
    #list_display = ('idResidencia', 'nombreDueño', 'fonoDueño')
    #list_editable = ('fonoDueño',)
admin.site.register(residencia)
admin.site.register(correspondencia)
#@admin.register(correspondencia)
#class correspondenciaAdmin(admin. ModelAdmin):
    #list_display = ('id_Residencia', 'Estado', 'fechaRecepcion', 'nombreConserje', 'nombreRemitente', 'nombreDestinatario')
    #list_editable = ('nombreConserje',)
    #list_filter = ('id_Residencia',)

