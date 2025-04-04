def change():
    expense = 23.75
    money = 100
    vuelto = money - expense 
    vuelto_pesos = int(vuelto)
    vuelto_centavos = int((vuelto - vuelto_pesos) * 100)

    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("") 
    print("Vuelto")
    print("")
    print("Pesos:")
    print(vuelto_pesos)
    print("Centavos:")
    print(vuelto_centavos)
