valor = int (input("Digite o valor do produto: "))
dinheiro = int (input("Digite o valor a ser pago: "))

class Troco():

    def valortroco(self, dinheiro, valor):
        return dinheiro - valor

    if valortroco > 0:
        print("O troco recebido é de:", valortroco)

    else
        print("O dinheiro não é suficiente para a compra do produto")

