
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='url-home'),
    path('', views.listaPacientes, name='url-lista-pacientes'),
    path('lista_view/<int:id>', views.listaView, name='url-lista-view'),
    path('newpaciente/', views.newPaciente, name='new-paciente'),
    path('editpaciente/<int:id>', views.editPaciente, name='edit-paciente'),
    path('deletepaciente/<int:id>', views.deletePaciente, name='delete-paciente'),
    

]
