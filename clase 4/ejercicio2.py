try:
    edad=int(input("ingrese su edad: "))
    print("su edad es:",edad)
except:
    print("ingrese valor numerico")
finally:
    print("esto siempre se ejecutal")
