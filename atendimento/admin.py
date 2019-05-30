from django.contrib import admin
# Register your models here.
from . models import Paciente
from . models import Medico
from . models import  Medicamento

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Medicamento)