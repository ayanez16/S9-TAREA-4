class Lista:
    def __init__(self,datos=[]):
        self.lista = datos

    def push(self,dato):
        self.lista.append(dato)

    def pop(self):
        dato = self.lista.pop()
        return dato

    def eliminarElemento(self,pos):
        if pos < 0 or pos >= len(self.lista):
            return None
        else:
            # self.lista = self.lista[0:pos] + self.lista[pos+1:]
            listaAux = []
            for ind in range(0,pos):
                listaAux += [self.lista[ind]]
            for ind in range(pos+1,len(self.lista)):
                listaAux += [self.lista[ind]]
            self.lista= listaAux
            return self.lista

    def insertarElemento(self,pos,valor):
        self.lista.insert(pos,valor)

    def buscar(self,buscado):
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele == buscado:
                enc=True
                break
        if enc ==True:return pos
        else:return -1

    def mostrar(self):
        for lista in self.lista:
            print(lista)

numeros = Lista()
numeros.push("4")
numeros.push("3")
numeros.push("5")
numeros.push("7")
numeros.push("10")
# numeros.insertarElemento(3,"9")
numeros.eliminarElemento(1)
numeros.mostrar()
# print(numeros.buscar("5"))
# print(numeros.pop())
# print(numeros.lista)