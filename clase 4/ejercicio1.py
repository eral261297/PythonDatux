lista=[1,2,3,4,5,6]
try:
    print(lista[2])
except Exception as e:
    #muestra de errores
    print(e)
else:
    print("funciona correctamente")
finally:
    print("siempre se ejecuta")