#objeto dentro de onjetos
class Pelicula:
    # constructor de clase
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo=titulo
        self.duracion=duracion
        self.lanzamiento=lanzamiento
        print('se ha creado la pelicula', self.titulo)
    def __str__(self):
        return '{} se estreno ({})'.format(self.titulo, self.lanzamiento)

class Catalogo:

    listaPeliculas=[] #esta lista contendrá objetos de la clase pelicula
    def __init__(self,pelicula):
        self.listaPeliculas.append(pelicula)

    def agregar(self, p): #p será un objeto pelicula
        self.listaPeliculas.append(p)

    def mostrar(self): 
        for p in self.listaPeliculas: #print toma por defecto str(p)
            print(p)
p=Pelicula("wankanda",2,2022)
p1=Pelicula("free",1,2021)

c1=Catalogo(p)
c1.agregar(p1)
c1.mostrar()