mulher1 = int(input("Digite a idade da primeira mulher: "))
mulher2 = int(input("Digite a idade da segunda mulher: "))
homem1 = int(input("Digite a idade do primeiro homem: "))
homem2 = int(input("Digite a idade do segundo homem: "))


if mulher1 > mulher2:
    print("Mulher mais velha: ", mulher1, "Produto das idades: ", mulher1 * homem2 )
else:
    print("Mulher mais velha: ", mulher2)

if homem1 > homem2:
    print("Homem mais velho: ", homem1, "Soma das idades: ", homem1 + mulher2)
else:
    print("Homem mais velho:", homem2)

