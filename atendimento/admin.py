from django.contrib import admin
# Register your models here.
from . models import Paciente
from . models import Medico

admin.site.register(Paciente)
admin.site.register(Medico)
