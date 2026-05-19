from django.contrib import admin

from .models import (
    Product,
    Categoria,
    Pedido,
    Opinion,
    Promocion,
    Inventario
)

admin.site.register(Product)
admin.site.register(Categoria)
admin.site.register(Pedido)
admin.site.register(Opinion)
admin.site.register(Promocion)
admin.site.register(Inventario)