from django.shortcuts import render
import requests
from .forms import FileForm

API = 'http://localhost:5000'

# Create your views here.
def index(request):
  return render(request, 'borrar.html')

def borrar(request):
  if request.method == 'POST':
    requests.post(API+'/borrar', data="")
  return render(request, 'borrar.html')

def cargar(request):
  if request.method == 'POST':
    form = FileForm(request.POST, request.FILES)

    if form.is_valid():
      txt = form.cleaned_data['file'].read()

      requests.post(API+'/cargarXML', data=txt)
  return render(request, 'cargar.html')

def procesamiento(request):
  return render(request, 'procesados.html')

def procesar(request):
  context = {
    'content': None
  }

  if request.method == 'GET':
    response = requests.get(API+'/procesarDatos')
    if response.status_code == 200:
      context['content'] = response.text

      return render(request, 'procesados.html', context)
    else:
      return render(request, 'procesados.html')

def datos(request):
  return render(request, 'datos.html')