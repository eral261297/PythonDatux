class Customer:
    edad=0
    correo=""
    def __init__(self,name,dni):
        self.name=name
        self.dni=dni
    def nameSpace(self):
        print(self.name)
    def __str__(self):
        return f'se llama {self.name}'
    def callEdad(self,edad):
        self.edad=edad
    def correo(self,correo):
        self.correo=correo

c1=Customer("gian","16467979")
c1.nameSpace()
print(c1.name)
print(c1)
print(type(c1))