from django.shortcuts import render
from . models import Entrada
from django.views import generic

# Create your views here.
def index(request):
    #num_entrada = Entrada.objects.all().count()

    return render(
        request,
        'index.html',
        #context={'numero_entradas': num_entrada},
    )

def ayuda(request):
    
    return render(
        request,
        'necesitoayuda.html',
    )

def amistadestoxicas(request):
    
    return render(
        request,
        'necesitoayuda2.html',
    )

def diferencias(request):
    
    return render(
        request,
        'necesitoayuda3.html',
    )

def suicidio(request):
    
    return render(
        request,
        'necesitoayuda4.html',
    )

def acososexual(request):
    
    return render(
        request,
        'necesitoayuda5.html',
    )

def redesSociales(request):
    
    return render(
        request,
        'necesitoayuda6.html',
    )

def paginasAyuda(request):
    
    return render(
        request,
        'necesitoayuda7.html',
    )              



def contacto(request):
    
    return render(
        request,
        'contacto.html',
    )


from django.views import generic

class EntradaDetailView(generic.DetailView):
    model = Entrada

class EntradaListView(generic.ListView):
    model = Entrada
    template_name = 'templates/contacto/entrada_list.html'
    queryset = Entrada.objects.all()
    paginate_by = 10