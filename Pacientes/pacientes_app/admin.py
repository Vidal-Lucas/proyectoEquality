from django.contrib import admin

from pacientes_app.models import Paciente

# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    list_display=("nombre","apellido","dni", "obra_soc")
    search_fields=("nombre","apellido","dni","obra_soc",)
    list_filter=("obra_soc",)


admin.site.register(Paciente,PacienteAdmin)