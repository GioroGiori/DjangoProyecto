from django.shortcuts import render
from .models import Personaje, Usuario
from datetime import datetime

# Create your views here.


def login(request):
    print("Login")
    context={}

    return render(request, "characters/login.html", context)


def loginData(request):
    print("Login")
    Usuarios=["admin, Gioro"]
    Contraseñas=["admin,123"]

    if request.method=="POST":
        print("Post")
        opcion=request.POST.get("opcion")

        if opcion=="Ingresar":
            print("Validar")


            usuario=request.POST["usuario"]
            contraseña=request.POST["contraseña"]

            if usuario in Usuarios and contraseña in Contraseñas:

                print("Validado")
                context={"usuario":usuario, "contraseña": contraseña}

                return render(request, "characters/quienesSomos.html", context)
            else:
                print("No validado")
                context={}
                return render(request, "characters/error.html", context)






def index(request):
    print("Estoy en el Index")
    context={}
    return render(request, 'characters/index.html', context)

def quienesSomos(request):
    print("QuienesSomos")
    context={}
    return render(request, 'characters/quienesSomos.html', context)


def colaborador(request):
    print("Se esta en la colaboración")
    context={}
    return render (request, 'characters/colaboradores.html', context)


def crud_personajes(request):

    print("hola  estoy en crud_alumnes...")
    personajes = Personaje.objects.all()  #select * from Alumne
    context = {'personajes': personajes}
    return render(request, 'characters/agregarPersonaje.html', context)

def agregarPersonaje(request):
    print("Estoy en agregar personaje")
    context={}
    if request.method=="POST":
        print("Post")
        opcion=request.POST.get("opcion", "")
        print("opcion="+opcion)

        #Listar
        if opcion=="Editar" or opcion=="Volver":
            personaje=Personaje.objects.all()
            context={'personaje': personaje}
            print("Enviando a List")
            return render(request, "characters/listarPersonaje.html", context)


        #Agregar

        if opcion=="Agregar":
            nombre=request.POST["nombre"]
            cumpleaños=request.POST["cumpleaños"]
            edad=request.POST["edad"]
            region=request.POST["region"]
            vision=request.POST["vision"]
            afiliacion=request.POST["afiliacion"]
            constelacion=request.POST["constelacion"]
            genero=request.POST["genero"]
            foto=request.FILES["foto"] 


            if region!="" and vision !="" and constelacion!="":

                personaje=Personaje()

                personaje.nombre=nombre
                personaje.fecha_cumpleaños=cumpleaños
                personaje.edad=edad
                personaje.region=region
                personaje.vision=vision
                personaje.afiliacion=afiliacion
                personaje.genero=genero
                personaje.foto=foto

                personaje.save()

                context={'mensaje': "Guardado"}

            else:
                context={'mensaje': "Error, no se pudo guardar, los datos estan vacios"}


        #Actualizar

        if opcion=="Actualizar":
            nombre=request.POST["nombre"]
            cumpleaños=request.POST["cumpleaños"]
            print("Cumpleaños= ", cumpleaños)
            edad=request.POST["edad"]
            region=request.POST["region"]
            vision=request.POST["vision"]
            afiliacion=request.POST["afiliacion"]
            constelacion=request.POST["constelacion"]
            genero=request.POST["genero"]
            foto=request.FILES.get("foto", False)

            if region!="" and vision !="" and constelacion!="":
                personaje=Personaje(nombre, cumpleaños, edad, region, vision, afiliacion, constelacion, genero, foto)

                personaje.save()

                context={'personaje': personaje, 'mensaje':"Personaje actualizado"}

            else:
                context={'mensaje': "Error, no se ha podido actualizar, verifique los datos"}

            return render(request, "characters/editarPersonaje.html", context)

    return render(request, "characters/agregarPersonaje.html", context)

def personaje_edit(request, pk):
    mensajes=[]
    errores=[]

    context={}
    personaje=Personaje.objects.all()

    personaje=Personaje.objects.get(id_personaje=pk)

    context={}

    if personaje:
        print("Se encontro al personaje")
        mensajes.append("Datos eliminados")

        context={'personaje': personaje, 'mensajes' : mensajes, 'errores' : errores}

        return render(request, 'characters/editarPersonaje.html', context)

    return render(request, 'characters/listarPersonaje.html', context)

def personaje_del(request, pk):
    mensajes=[]
    errores=[]
    personaje=Personaje.objects.all()
    try:
        personaje=Personaje.objects.get(id_personaje=pk)
        context={}
        if personaje:
            personaje.delete()
            mensajes.append("Datos elimiados")

            context={'personaje': personaje, 'mensajes':mensajes, 'errores': errores}


            return render(request, 'characters/listarPersonaje.html', context)

    except:
        print("Error, Personaje no existe")

        errores.append("Personaje no encontrado")

        context={'personaje': personaje, 'mensajes': mensajes, 'errores': errores}

        return render(request, 'characters/listarPersonaje.html', context)


def listarPersonaje(request):
    print("hola  estoy en personaje...")
    personajes = Personaje.objects.all()  
    context = {'personaje': personajes}
    return render(request, 'characters/listarPersonaje.html', context)


def personajes(request): 
    print("hola  estoy en personaje...")
    personajes = Personaje.objects.all()  
    context = {'personaje': personajes}
    return render(request, "characters/personajes.html",context)

def administracion(request):
    print("Adminisración")
    context={}
    return render(request, 'characters/administracion.html', context)

    
def agregarUsuario(request):
    print("Estoy en agregar personaje")
    context={}
    if request.method=="POST":
        print("Post")
        opcion=request.POST.get("opcion", "")
        print("opcion="+opcion)


        if opcion=="Agregar":
            nombre=request.POST["nombre"]
            contraseña=request.POST["contraseña"]


            if nombre!="" and contraseña!="":
                usuario=Usuario


                usuario.nombre=nombre
                usuario.contraseña=contraseña


                usuario.save()

                context={'mensaje': "Guardado"}

            else:
                context={'mensaje': "Error, no se pudo guardar, los datos estan vacios"}


        return render(request, "characters/crearUsuario.html", context)

