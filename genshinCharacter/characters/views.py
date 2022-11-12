from django.shortcuts import render

# Create your views here.


def index(request):
    print("Estoy en el Index")
    context={}
    return render(request, 'characters/index.html', context)
