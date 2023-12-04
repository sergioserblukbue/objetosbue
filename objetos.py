from datetime import datetime
class mascotas:
    def __init__(self,nombre, tipo, dni_propietario, sonido,anio_nac):
        self.nombre=nombre
        self.tipo=tipo
        self.dni_propietario=dni_propietario
        self.sonido=sonido
        self.anio_nac=anio_nac
    def comunicarse(self):
        print(f"{self.nombre} esta {self.sonido}")
    def obtener_edad(self):
        anio=datetime.now().year
        print(type(anio))
        print(f"la mascota tiene {int(anio) - int(self.anio_nac) } años")
    def __str__(self):
        return "nombre: " + self.nombre + " año nac: " + str(self.anio_nac)
        
mimascota=mascotas("coca","perro", "45639963", "ladrando",2010)
mascotadeJuan=mascotas("felpita","gato","54675576","maullando",2015)
mimascota.comunicarse()
mascotadeJuan.comunicarse()
print(f"el dni del dueño de {mimascota.nombre} es {mimascota.dni_propietario}")
print(mimascota)
print(mascotadeJuan)
anio=anio=datetime.now().year
mimascota.obtener_edad()
print(mimascota)
print(mascotadeJuan)