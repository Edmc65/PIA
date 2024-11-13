from django.shortcuts import render

def index(request):
    return render(request, 'mi_app/index.html')

def contacto(request):
    return render(request, 'mi_app/Contacto.html')

def productos(request):
    return render(request, 'mi_app/Productos.html')

def sobre_nosotros(request):
    return render(request, 'mi_app/SobreNosotros.html')

def tienda(request):
    return render(request, 'mi_app/Tienda.html')