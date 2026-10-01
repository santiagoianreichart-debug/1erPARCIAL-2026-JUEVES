from datetime import date, timedelta


class KwikEMart:
    def __init__(self):
        self.secciones = {
            "Bebidas": [],
            "Snacks": [],
            "Conveniencia": []
        }

    def agregar(self, producto, seccion):
        self.secciones[seccion].append(producto)

    def remover(self, id_producto):
        for seccion in self.secciones:
            for producto in self.secciones[seccion]:
                if producto.id_producto == id_producto:
                    self.secciones[seccion].remove(producto)
                    return

    def actualizar_stock(self, id_producto, stock):
        for seccion in self.secciones:
            for producto in self.secciones[seccion]:
                if producto.id_producto == id_producto:
                    producto.stock = stock
                    return

    def remover_por_vencer(self):
        hoy = date.today()
        limite = hoy + timedelta(days=1)
        cantidad = 0

        for seccion in self.secciones:
            for producto in self.secciones[seccion][:]:
                if hoy <= producto.fecha_vencimiento <= limite:
                    self.secciones[seccion].remove(producto)
                    cantidad += 1

        return cantidad