def fibo(num):
    lista = list()
    lista.append(1)
    lista.append(1)
    f = 0
    for i in range(num - 2):
        f = lista[i] + lista[i + 1]
        lista.append(f)

    print('Secuencia: ', lista)
    print("El número es: ", fibo(num))