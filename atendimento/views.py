from django.shortcuts import render
from . models import Paciente
from . models import Medico
from . models import Medicamento


# Create your views here.

def home(request):
    return render(request,'home.html')
    
def paciente_list(request):
    pacientes=Paciente.objects.all()
    return render(request,'paciente/list.html',{'pacientes':pacientes})
    
def paciente_show(request,id):
    return render(request,'paciente/show.html',{'id':id})

def medico_list(request):
    medicos=Medico.objects.all()
    return render(request,'medico/list.html',{'medicos':medicos})
     
def medico_show(request,id):
    return render(request,'medico/show.html',{'id':id})

def agendamento_list(request):
    return render(request,'agendamento/list.html')

def medicamentos_list(request):
    medicamentos=Medicamento.objects.all()
    return render(request,'medicamentos/list.html',{'medicamentos':medicamentos})