class GestionInventario:
    def __init__(self):
        self.inventario = {}

    def añadir_producto(self, producto, cantidad):
        if producto in self.inventario:
            self.inventario[producto] += cantidad
        else:
            self.inventario[producto] = cantidad

    def eliminar_producto(self, producto):
        self.inventario.pop(producto, None)

    def consultar_producto(self, producto):
        return self.inventario.get(producto, 'Producto no existe en el inventario.')

    def mostrar_inventario(self):
        print('--- Inventario ---')
        for producto, cantidad in self.inventario.items():
            print(f'{producto}: {cantidad}')
        print('--- ---------- ---')

gestion = GestionInventario()
gestion.añadir_producto('Manzanas', 10)
gestion.añadir_producto('Peras', 5)
gestion.añadir_producto('Manzanas', 5)
gestion.añadir_producto('Naranjas', 30)

print('Consultar Manzanas:', gestion.consultar_producto('Manzanas'))
gestion.mostrar_inventario()

gestion.eliminar_producto('Peras')
print('Inventario despues de eliminar las peras:')
gestion.mostrar_inventario()

