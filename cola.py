class Cola:
    def __init__(self,tamaño=9):
        self.cola = []
        self.tope = 0
        self.size = tamaño

    def empty(self):
        return self.tope == 0

    def push(self,dato):
        self.cola.append(dato)
        self.tope += 1

    def pop(self):               #desencolar
        if self.empty():
            return("La cola esta vacia")
        else:
            return self.cola.pop(0)

    def show(self):
        for top in range(self.tope):
            print("[{}]".format(self.cola[top]))

    def buscar(self,buscado):
        enc=False
        for pos,ele in enumerate(self.cola):
            if ele == buscado:
                enc=True
                break
        if enc ==True:return pos
        else:return -1

    def longitud(self):
        return self.tope

cola1 = Cola(10)
cola1.push("4")
cola1.push("5")
cola1.push("7")
cola1.push("10")
# print(cola1.cola)
cola1.show()
print(cola1.buscar("5"))
print(cola1.longitud())
