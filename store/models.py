from django.db import models


# =========================
# CATEGORÍAS
# =========================
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


# PRODUCTOS
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    categoria = models.ForeignKey(
    Categoria,
    on_delete=models.CASCADE,
    related_name='productos',
    null=True,
    blank=True
    )
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# PEDIDOS
class Pedido(models.Model):
    cliente = models.CharField(max_length=100)
    productos = models.ManyToManyField(Product)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id}"



# OPINIONES

class Opinion(models.Model):
    usuario = models.CharField(max_length=100)
    comentario = models.TextField()
    calificacion = models.IntegerField()

    def __str__(self):
        return self.usuario



# PROMOCIONES

class Promocion(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    descuento = models.IntegerField()

    def __str__(self):
        return self.titulo



# INVENTARIO

class Inventario(models.Model):
    producto = models.OneToOneField(Product, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.producto.name