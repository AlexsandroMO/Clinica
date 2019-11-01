from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Paciente
from .forms import PacienteForm
from django.contrib import messages
from django.core.paginator import Paginator



def home(request):
    pacientes = Paciente.objects.all()
    return render(request, 'clinica/home.html', {'pacientes': pacientes})


def listaPacientes(request):
    search = request.GET.get('search')
    if search:
        pacientes = Paciente.objects.filter(nome__icontains=search)
    else:
        paciente_list = Paciente.objects.all()
        paginator = Paginator(paciente_list, 3) #quantidde de linhas
        page = request.GET.get('page')
        pacientes = paginator.get_page(page)

    return render(request, 'clinica/lista-pacientes.html', {'pacientes': pacientes})


def listaView(request, id):
    pacientes = get_object_or_404(Paciente, pk=id)

    cpf = pacientes.cpf
    cpf_number = '{}.{}.{}-{}'.format(cpf[0:3],cpf[3:6], cpf[6:9],cpf[9:11])

    cep = pacientes.cep
    cep_number = '{}-{}'.format(cep[0:5],cep[5:8])

    return render(request, 'clinica/lista-view.html', {'pacientes': pacientes, 'cpf_number': cpf_number, 'cep_number': cep_number})


def newPaciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)

        if form.is_valid():
            pacientes = form.save(commit=False)
            pacientes.save()
            return redirect('/')

    else:
        form = PacienteForm()
        return render(request, 'clinica/addpaciente.html', {'form': form})


def editPaciente(request, id):
    pacientes = get_object_or_404(Paciente, pk=id)
    form = PacienteForm(instance=pacientes)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=pacientes)

        if form.is_valid():
            pacientes.save()
            return redirect('/')
        else:
            return render(request, 'clinica/edit-paciente.html', {'form': form, 'pacientes': pacientes})

    else:
        return render(request, 'clinica/edit-paciente.html', {'form': form, 'pacientes': pacientes})


def deletePaciente(request, id):
    pacientes = get_object_or_404(Paciente, pk=id)
    pacientes.delete()

    messages.info(request, 'Paciente deletado com sucesso.')
    return redirect('/')





# def listaPacientes(request):
#     paciente_list = Paciente.objects.all()
#     paginator = Paginator(paciente_list, 3) #quantidde de linhas
#     page = request.GET.get('page')
#     pacientes = paginator.get_page(page)

#     return render(request, 'clinica/lista-pacientes.html', {'pacientes': pacientes})