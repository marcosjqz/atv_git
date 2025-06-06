from django.contrib import admin
from .models import Paciente, Especialidade, Medico, Consulta, Prontuario

# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'cpf', 'telefone', 'endereco', 'email', 'created_at')
    search_fields = ('nome', 'cpf')
      
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'telefone', 'email', 'created_at')
    search_fields = ('nome', 'crm')

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'data_hora', 'motivo', 'created_at')

class ProntuarioAdmin(admin.ModelAdmin):
    list_display = ('consulta', 'diagnostico', 'prescricao', 'observacoes', 'created_at')    

class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')    

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(Prontuario, ProntuarioAdmin)
admin.site.register(Especialidade, EspecialidadeAdmin)