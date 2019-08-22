def lernumero():
    numeros = [] #lista
    numero = 0

    for i in range (numeros, 10):
    numero = int(input("Digite 10 números: "))
    numeros.append(numero)

    maiornumero = max(numeros)
    menornumero = min(numeros)
    print("O maior número é: ", maiornumero)
    print("O menor número é: ", menornumero)
