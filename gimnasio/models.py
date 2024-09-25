from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre  # Asegúrate de que esto sea un string

class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre  # Debe devolver un string

class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)  # Relación con Entrenador
    horario = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre  # Esto también debe ser un string
