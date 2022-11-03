from django.urls import path
from AppFamiliares import views

urlpatterns = [
    path('Familiares/', views.mostrar_familiares),
]
