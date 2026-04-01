
while True:
    precio=float(input("hola , registre el precio de su producto: ")) 
    print("1.Alimentos\n2.Ropa\n3.Electronica\n4.Hogar\n5.Salir")
    categoria=int(input("ingre su categoria: "))

    if categoria == 1:
        print("descuento: 5% ")
        precio_final= precio - (precio * 0.05)

    elif categoria == 2:
        print("descuento: 10% ")
        precio_final= precio - (precio * 0.10)

    elif categoria == 3:
        print("descuento: 15% ")
        precio_final= precio - (precio * 0.15)

    elif categoria == 4:
        print("descuento: 8% ")
        precio_final= precio - (precio * 0.08)
    elif categoria == 5:
        print("saliendo del programa....")
        break
    else:
        print("XXX CATEGORIA NO EXITE, ERROR XXX")
        continue

    print("el precio de su compra: ",precio_final)



