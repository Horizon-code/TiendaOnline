from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.
#clase que declara que campos se quieren enseñar en el gestor Admin
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","telefono")
    #barra de búsqueda en el panel admin
    search_fields=("nombre", "telefono")

class ArticulosAdmin(admin.ModelAdmin):
    #filtro por campos("seccion", etc..)
    list_filter=("seccion",)

class PedidosAdmin(admin.ModelAdmin):
    #le indicamos que campos queremos ver
    list_display=("numero", "fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha"
    
  


#Registrar para tener disponible los modelos  (clientes,articulos,pedidos,...) desde el panel de administracion
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
