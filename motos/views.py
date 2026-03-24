from django.shortcuts import render, redirect
from .models import Moto
from .forms import MotoForm

# Create your views here.
def list_motos(request):
    motos = Moto.objects.all()
    return render(request, 'motos.html', {'motos': motos})

def create_motos(request):
    form = MotoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_motos')
    return render(request, 'moto-form.html', {'form': form})