
numero_ingresados=[]
while True:
    entrada=(input("selecciona calcular o salir: "))
    
    if entrada.lower()=="salir":
        print("SALIENDO DEL PROGRAMA")
        break
    if entrada.lower()=="calcular":
            while True:
                numero=int(input("ingresa un numero(-1 para finalizar): "))
                if numero == -1: 
                     break
                numero_ingresados.append(numero)


            mayor=0
            menor=9999999999
            suma=0
            par=0
            impar=0

            for num in numero_ingresados:
                    if num > mayor:
                        mayor = num
                    if num < menor:
                        menor = num

                    if num % 2 == 0:
                         par += 1
                    else:
                         impar += 1
                         
                    suma+=num
            promedio= suma/len(numero_ingresados)

                   
           

            print("numero mayor: ", mayor)
            print("numero menor: ", menor)
            print("su promedio es: ", promedio)
            print("numero impar: ", impar)
            print("numero par: ", par)
