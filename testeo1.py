#Este va a ser una calculadora tpipica.
validar=False
while not validar:
    try:
        n1= float(input("Ingrese el primero numero: "))
        n2= float(input("Ingrese el segundo numero: "))
        validar=True
    except ValueError:
        print("Debe ingresar numero validos")

opcion = input("Ingrese la operacion que desea realizar: ").strip().lower()

if opcion=="suma":
    print(n1+n2)
elif opcion=="resta":
    print(n1-n2)
elif opcion=="multiplicar":
    print(n1*n2)
elif opcion=="dividir":
    if n2==0:
        print("No se puede dividir por 0")
    else:
        print(n1/n2)
else:
    print("Ingrese una operacion valida")
    