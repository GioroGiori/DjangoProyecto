from django.db import models

# Create your models here.

'''
def Somos():
'''
def cargarFoto(instance, filename):
    return "fotos/foto_{0}_{1}".format(instance.id_personaje, filename )



class Personaje(models.Model):
    id_personaje=models.AutoField(db_column='id_personaje', primary_key=True)
    fecha_cumpleaños=models.DateField(blank=True, null=True)
    characterID=models.CharField(max_length=20, blank=False, unique=True)
    nombre=models.CharField(max_length=20, blank=True)
    edad=models.CharField(max_length=10, blank=True, null=True)
    region=models.CharField(max_length=20, blank=False, null=False)
    vision=models.CharField(max_length=10, blank=False, null=False)
    afiliacion=models.CharField(max_length=20, blank=True)
    constelacion=models.CharField(max_length=30, blank=False, null=False)
    genero = models.CharField(max_length=10, blank=True, null=True) 
    foto  = models.ImageField(upload_to='fotos', blank=True, null=True)


    def __str__(self):
        return self.id_personaje+", "+ str(self.fecha_cumpleaños)+", "+ self.characterID+", "+\
                self.nombre+", "+ self.edad+", "+ self.region+", "+ self.region+", "+ self.vision+", "+\
                self.afiliacion+", "+self.constelacion+", "+self.genero+", "+self.foto.__str__()
            

