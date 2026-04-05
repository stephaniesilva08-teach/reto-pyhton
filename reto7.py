lista_1=[]
lista_2=[]
lista_3=[]

def ingresar_elementos1():
    numero1=int(input("ingrese numeros (lista 1): "))
    lista_1.append(numero1)
    return lista_1

def ingresar_elementos2():
    numero2=int(input("ingrese numero (lista 2): "))
    lista_2.append(numero2)
    return lista_2

def suma_elementos(i):
    suma=lista_1[i]+lista_2[i]
    lista_3.append(suma)
    return lista_3


while True:
    numero1=int(input("cantidad numeros lista 1: "))
    numero2=int(input("cantidad numeros lista 2: "))
    if numero1 != numero2:
        print("XXXX LAS LISTAS TIENEN QUE SER IGUAL EN CANTIDAD XXXX")
        break

    if numero1 == numero2:
        for i in range(numero1):
            lista1=ingresar_elementos1()
        for i in range(numero2):
            lista2=ingresar_elementos2()
        for i in range(numero1):
            resultado=suma_elementos(i)

    break
            

print("tu lista 1: ", lista1)
print("tu lista 2: ", lista2)
print("resultado: ", resultado)

      



            
            
    