from django.db import models

# Create your models here.

'''
def Somos():
'''





def cargarFoto(instance, filename):
    return "fotos/foto_{0}_{1}".format(instance.idProducto,filename)
