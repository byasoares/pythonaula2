numeros = []
numero = 0
maior = max(numeros)

numero = int(input("Digite o primeiro número: "))
numeros.append(numero)

for i in range (9):
    numero = int(input("Digite os próximos números: "))
    numeros.append(numero)
print("O maior número da lista é: ", maior)