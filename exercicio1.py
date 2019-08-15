listanome = []
listanota1 = []
listanota2 = []
listanota3 = []

aluno = 0
nota1 = 0
nota2 = 0
nota3 = 0
calculo = 0

def matricular():
    aluno = (input("Digite o nome do aluno: "))
    listanome = aluno
    nota1 = (input("Digite a primeira nota: "))
    listanota1 = nota1
    nota2 = (input("Digite a segunda nota: "))
    listanota2 = nota2
    nota3 = (input("Digite a terceira nota: "))
    listanota3 = nota3


def calculo(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

#if calculo >= 6
    #print("Aluno aprovado!")
#else print ("Aluno reprovado!")
