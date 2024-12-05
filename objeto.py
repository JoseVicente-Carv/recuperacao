class Pessoa:
    nome: str
    idade: int
    peso: float

p1 = Pessoa()

p1.nome = "Martha"
p1.idade = 18
p1.peso = 89.4

aluno = Pessoa()

aluno.nome = input("Escreva o nome do aluno: ")
aluno.idade = int(input("insira o nome do aluno: "))
aluno.peso = float(input("Insira o peso do aluno: "))