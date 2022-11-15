from distutils.command.upload import upload
from email.mime import image
from multiprocessing import context
from typing import Container
from urllib import request
from django.shortcuts import render
from django.db import models


# Create your views here.

#Clases

class Character:
    Imagen=models.ImageField(null=True, blank=False, upload_to="img/")
    characterID=""
    nombre=""
    edad=0
    altura=0
    region=""
    vision=""
    jugable=""
    afiliacion=""
    cumpleaños=""
    constelacion=""

    def __init__(self, Imagen, characterID, nombre, edad, altura, region, vision, jugable, afiliacion, cumpleaños, constelacion):

        self.Imagen=Imagen
        self.characterID = characterID
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.region = region
        self.vision = vision
        self.jugable = jugable
        self.afiliacion = afiliacion
        self.cumpleaños = cumpleaños
        self.constelacion = constelacion

    def getImage(self):
        return self.Imagen
    def getCharaID(self):
        return self.characterID

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getAltura(self):
        return self.altura

    def getRegion(self):
        return self.region
        
    def getVision(self):
        return self.vision

    def getJugable(self):
        return self.jugable

    def getAfiliacion(self):
        return self.afiliacion

    def getCumpleaños(self):
        return self.cumpleaños

    def getConstelacion(self):
        return self.constelacion

    def toString(self):
        return self.characterID+", "+self.nombre+", "+self.edad+", "+self.altura+", "+self.region+", "+self.vision+", "+self.jugable+", "+self.afiliacion+", "+self.cumpleaños+", "+self.constelacion


charaID1= Character("10000038", "Albedo", 19, 162, "Mondstadt", "Geo", "Jugable", "Caballero de Favonius/Editorial Yae", "13/09", "Princeps Cretaceus")

charaID2= Character("10000034", "Noelle", 15, 158, "Mondstadt", "Geo", "Jugable", "Caballero de Favonius", "21/03", "Parma Cordis")

charaID3= Character("10000043", "Sacarosa", 18, 155, "Mondstadt", "Anemo", "Jugable", "Caballero de Favonius", "26/11", "Ampulla")

charaID4= Character("10000037", "Ganyu", 3000, 158, "Liyue", "Cryo", "jugable", "Pabellón Yuehai/Siete Estrellas de Liyue/Adeptus de Liyue", "2/12", "Sinae Unicornis")

charaID5= Character("10000042", "Keching", 17, 158, "Liyue", "Electro", "Jugable", "Siete Estrellas de Liyue", "20/11", "Trulla Cementarii")

charaID6= Character("10000052", "Ei Raiden", 2000, 172, "Inazuma", "Electro", "Jugable (Como Shogun Raiden", "Ciudad de Inazuma/Shogunato de Inazuma,Arcontes", "26/06", "Imperatrix Umbrosax")

charaID7= Character("10000067", "Collei", 16, 156, "Sumeru", "Dendro", "Jugable", "Academia de Sumeru","8/5", "Leptailurus Cervarius")

charaID8= Character("10000007", "Lumine", 500, 156, "Viajera de otro mundo", "Todas", "Jugable", "Ninguna", "1/01", "Viatrix")

charaID9= Character("10000033", "Tartaglia", 21, 189, "Snezhnaya", "Hydro", "Jugable", "Fatui/ Once Heraldos de los Fatui", "20/07", "Monocerus Caeli")
2
charaID10= Character("10000075", "Mika", 11, 160, "Mondstadt","Cryo", "No Jugable (NPC)", "Caballeros de Favonius", "19/09", "none")

personajes= [charaID1, charaID2, charaID3, charaID4, charaID5, charaID6, charaID7, charaID8, charaID9, charaID10]


        






#Views
def login(request):
    print("login page...")
    context={}

    return render(request,"characters/login.html", context)

def error(request):
    print("Error")
    context={}

    return render(request, "characters/error.html", context)

def index(request):
    print("Index")
    context={}

    return render(request, "characters/index.html", context)


def loginData(request):
    print("Login")
    Usuarios=["GioroGiori", "Gioro", "Giori", "Crismy", "admin", "root", "GioroGioriCrismy", "GiovanniRomero"]
    Contraseñas=["123", "GioroGioriCrismy28!", "GioroGiori28!", "Gioro_Giori_Crismy", "root", "admin", "GioroGioriCrismy28", "GioroGiori28"]

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

                return render(request, "characters/index.html", context)

    
            else:
                print("No validado")
                context={}
                return render(request, "characters/error.html", context)




def characterAdd(request):
    print("Hora de agregar personajes de Genshin Impact :D")
    context={}

    if request.method=="POST":
        print("Post")
        opcion=request.POST.get("opcion","")

        print("opcion= "+opcion)





        if opcion=="Agregar":
            characterID=request.POST["characterID"]
            nombre=request.POST["nombre"]
            edad=request.POST["edad"]
            altura=request.POST["altura"]
            region=request.POST["region"]
            vision=request.POST["vision"]
            jugable=request.POST["jugable"]
            afiliacion=request.POST["afiliacion"]
            cumpleaños=request.POST["cumpleaños"]
            constelacion=request.POST["constelacion"]


            if characterID !="" and nombre !="" and edad !="" and altura !="" and region !="" and vision !="" and jugable !="" and afiliacion !="" and cumpleaños !="" and constelacion !="":

                chara= Character(characterID, nombre, edad, altura, region, vision, jugable, afiliacion, cumpleaños, constelacion)

                personajes.append(chara)


                context={'mensaje': "Personaje guardado!"}
            else:
                context={'mensaje':"Error: Campos vacios"}


            return render(request, "characters/index.html",context)

        if opcion=="Editar" or opcion=="Volver":
            context={'personajes': personajes}
            print("Vamos a editar personajes en characters_edit")
            return render(request, "characters/characters_list.html", context)

        if opcion=="Actualizar":
            characterID=request.POST["characterID"]
            nombre=request.POST["nombre"]
            edad=request.POST["edad"]
            altura=request.POST["altura"]
            region=request.POST["region"]
            vision=request.POST["vision"]
            jugable=request.POST["jugable"]
            afiliacion=request.POST["afiliacion"]
            cumpleaños=request.POST["cumpleaños"]
            constelacion=request.POST["constelacion"]

            if characterID !="" and nombre !="" and edad !="" and altura !="" and region !="" and vision !="" and jugable !="" and afiliacion !="" and cumpleaños !="" and constelacion !="":
                
                chara= Character(characterID, nombre, edad, altura, region, vision, jugable, afiliacion, cumpleaños, constelacion)
                pos=0

                for x in personajes:
                    if x.getCharaID()== chara.getCharaID():
                        personajes.remove(x)
                        personajes.insert(pos, chara)
                        break
                pos=pos+1

                context={'chara':chara, 'mensaje' : "Los datos han sido actualizados"}

            else:
                context={'mensaje': "Error"}

            return render(request, "characters/characters_edit.html", context)





def characters_del(request, pk):
    print("Eliminando personaje... pk="+pk)

    mensajes=[]
    errores=[]

    try:
        context={}
        sw=0

        for chara in personajes:
            if chara.getCharaID()== pk:
                sw=1
                personajes.remove(chara)
                mensajes.append("Personaje eliminado")
                print("characters_del personaje eliminado")

        if sw==0:
            errores.append("Error, el personaje no existe")
            print("characters_del personaje no eliminado")

        context={'personajes': personajes, 'mensaje': mensajes, 'errores':errores}
        
        return render(request, 'characters/characters_list.html',context)
    
    except:
        print("Error, el personaje no existe no existe")
        errores.append("Error, personaje no encontrado")
        context={'personajes': personajes, 'mensaje': mensajes, 'errores':errores}
        return render(request, 'characters/characters_list.html',context)



def characters_edit(request, pk):
    print("Estoy en character_edit pk="+ pk)

    mensajes=[]
    errores=[]
    context=[]


    for chara in personajes:
        if chara.getCharaID()==pk:
            print("Se ha encontrado al personaje, llendo a editar....")

            context={'chara': chara, 'mensajes':mensajes, 'errores':errores}

            break

    return render(request,'characters/characters_edit.html', context)
