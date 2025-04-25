from django.db import models

class Producto(models.Model):
    CATEGORIAS = [
        ('polaroid', 'Foto Polaroid'),
        ('tupper', 'Tupper para tortas'),
        ('llavero', 'Llavero'),
        ('sticker', 'Sticker'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre