from django.shortcuts import render, redirect
# from django.views.generic import TemplateView
from django.views import View

# Create your views here.
from calculadora_app.models import ModeloEjemplo

class ClaseListado(View):
    def get(self,request):
        contexto={'modelos':ModeloEjemplo.objects.all()}
        return render(request,'listado.html',contexto)

class ClaseBorrar(View):
    def get(self,request,id):
        antiguo=ModeloEjemplo.objects.get(id=id)
        antiguo.delete()
        return redirect('listado')

class ClaseEditar(View):
    def get(self,request,id):
        antiguo=ModeloEjemplo.objects.get(id=id)
        contexto = {'modelo': antiguo, 'mensaje': ''}
        return render(request, 'formulario.html', contexto)

    def post(self,request,id):
        antiguo = ModeloEjemplo.objects.get(id=id)
        antiguo.id1=request.POST['id1']
        antiguo.id2 = request.POST['id2']
        antiguo.save() # actualizando
        return redirect('listado')

class ClaseVista(View):
    def get(self,request):
        nuevo=ModeloEjemplo()
        contexto = {'modelo': nuevo,'mensaje':''}
        return render(request,'formulario.html',contexto)

    def post(self,request):
        nuevo = ModeloEjemplo(
            id1=request.POST['id1']
            , id2=request.POST['id2']
        )
        contexto={'modelo':nuevo,'mensaje':'modelo insertado'}
        nuevo.save() # guarde en la base de datos.
        return redirect('listado')
        # return render(request,'formulario.html',contexto)

def formulariosimple(request):
    if request.method=='POST':
        id1 = request.POST['id1']
        id2 = request.POST['id2']
    else:
        id1=''
        id2=''
    contexto = {'id1': id1, 'id2': id2}
    return render(request, 'formulario.html', contexto)