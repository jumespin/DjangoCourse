from django.contrib import admin
from .models import AutorDb, FraseDb, ProfesionDb

# Register your models here.

admin.site.site_header = "Quotes administrator site"
admin.site.index_title = "Gestor de quotes by Doofesmith malvados & asociados"
admin.site.site_title = "Una compañía responsable"

@admin.register(ProfesionDb)
class ProfesionAdmin(admin.ModelAdmin):
     list_display = ["nombre"]
     fields = ["nombre"]

class FraseInLine(admin.TabularInline):
        model = FraseDb
        extra = 1

class AutorAdmin(admin.ModelAdmin):
    fields = ("nombre","fecha_nacimiento", "fecha_fallecimiento", "profesion", "nacionalidad" )
    list_display = ["nombre", "fecha_nacimiento"]

    inlines = [FraseInLine]

    def actualizar_o(self, request, queryset):
        for obj in queryset:
            if "O" in obj.nombre:
                nombre1 = obj.nombre
                obj.nombre = nombre1.replace("O","o")
                obj.save()

        self.message_user(request, "Exitosamente")
    
    actualizar_o.short_description = "Actualizar letras O"

    actions = ["actualizar_o"]

admin.site.register(AutorDb,AutorAdmin)

@admin.register(FraseDb)
class FraseAdmin(admin.ModelAdmin):
    fields = ("quote", "autor_fk")
    list_display = ["quote"]