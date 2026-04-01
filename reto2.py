def es_primo(numero):
    if numero <2:
        return False
    for i in range (2,numero):
        if numero % i == 0:
            return False 
    return True 

def obtener_divisores(numero):
      divisores=[]
      for i in range(1,numero+1):
            if numero % i == 0:
                  divisores.append(i)
      return divisores
        


while True:
    numero=(input("ingrese un numero o salir: "))
    if numero.lower()== "salir":
          print("SALIENDO DEL PROGRAMA...")
          break
    try:
          numero=int(numero)
          if numero < 1:
                print ("XXX ERROORRR XXX NUMERO POSITIVO MAYOR A 0")
                continue 
    except ValueError:
          print("XXX ERRORRRR XXX INGRESE NUMERO ENTERO")
          continue 
    
    divisores= obtener_divisores(numero)
    print(divisores)

    if es_primo(numero):
        print("ES NUMERO PRIMO")
               
    else:
    
        print("NO ES PRIMO")
    
   
          

            



