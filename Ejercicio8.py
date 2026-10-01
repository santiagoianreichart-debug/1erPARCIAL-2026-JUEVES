class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig


class IteradorListaEnlazada:
    def __init__(self, nodo):
        self.actual = nodo

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration

        dato = self.actual._elem
        self.actual = self.actual._nxt
        return dato


class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(0)

    def agregar(self, dato):
        actual = self.header

        while actual._nxt is not None:
            actual = actual._nxt

        actual._nxt = Nodo(dato)

    def remover(self, dato):
        anterior = self.header
        actual = self.header._nxt

        while actual is not None:
            if actual._elem == dato:
                anterior._nxt = actual._nxt
                return

            anterior = actual
            actual = actual._nxt

    def __iter__(self):
        return IteradorListaEnlazada(self.header._nxt)