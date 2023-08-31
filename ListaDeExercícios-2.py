# Nome: Ian Arley Silva Domingos De Sousa
# Matéria: Estrutura de dados em python
# Professor: Nisston Moares

# Exercício 1

import math
class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return round(math.pi, 2) * self.raio**2    

while True:    
    escolha = int(input("Escolha uma opção:\nDigite 1 para seguir com o programa do calculo da área do círculo.\nDigite 2 para encerrar o programa\nDigite aqui a opção escolhida: "))
    if escolha == 1:
        Raio = float(input("Digite o valor do raio de uma circunferência para que seja calculada sua área: "))
        circulo = Circulo(Raio)
        Area = circulo.calcular_area()
        print(f"A área do círculo é: {Area} metros quadrados")
    
    if escolha == 2:
        break

# Exercício 2
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"    
    
livro1 = Livro("Dom Quixote", "Miguel de Cervantes")
print(livro1.detalhes())

livro2 = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling")
print(livro2.detalhes())

# Exercício 3
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

while True:    
    escolha = int(input("Escolha uma opção:\nDigite 1 para seguir com o programa do calculo da área do retângulo.\nDigite 2 para encerrar o programa\nDigite aqui a opção escolhida: "))
    if escolha == 1:
        Base = float(input("Digite o valor da base para que seja calculada a área do retângulo"))
        Altura = float(input("Digit o valor da altura para que seja calculada a área do retângulo: "))
        retangulo = Retangulo(Base, Altura)
        Area = retangulo.calcular_area()
        print(f"A área do retângulo é: {Area}")   
    if escolha == 2:
        break

# Exercício 4
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

class ContaBancaria:

    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular

    def depositar(self, deposito):
        self.saldo += deposito

    def sacar(self, saque):
        self.saldo -= saque

while True:
    escolha = int(input("Escolha uma das opções a seguir:\nPara continuar o programa digite 1.\nPara encerrar o programa digite 2.\nDigite aqui sua escolha: "))
    if escolha == 1:
        Titular = input("Digite o aqui o seu nome completo:")
        Saldo = float(input("Digite aqui o saldo atual da sua conta: "))
        conta = ContaBancaria(Saldo, Titular)
        escolha2 = int(input("Escolha uma das opções a seguir:\nPara depositar um valor digite 1.\nPara sacar um valor digite 2.\nDigite aqui sua escolha: "))
        if escolha2 == 1:
            ValorDepositado = float(input("Digite o valor que será adicionado a sua conta: "))
            SaldoAtual = conta.depositar(ValorDepositado)
            print(f"Após o depósito  na conta do titular {Titular} saldo final da sua conta é: ${conta.saldo}")

        if escolha2 == 2:
            ValorSacado = float(input("Digite o valor retirado da sua: "))
            SaldoAtual = conta.sacar(ValorSacado)
            print(f"Após o saque na conta do titular {Titular} saldo final da sua conta é: ${conta.saldo}")

    if escolha == 2:
        print("Programa encerrado.")
        break

# Exercício 5
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self, nome):
        return f"Olá {nome} tudo bão?"
    
Nome = input("Digite aqui o seu nome para receber uma bela mensagem: ")
pessoa = Pessoa(Nome, 0)
mensagem = pessoa.falar(pessoa.nome)
print(mensagem)

# Exercício 6
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        total = self.preco * self.quantidade
        return f"O valor total do produto {self.nome} é R${total}"

while True:
    escolha = int(input("Escolha uma opção:\nDigite 1 para seguir com o programa do calculo de valor total gasto na compra de uma quantidade de determinado produto.\nDigite 2 para encerrar o programa\nDigite aqui a opção escolhida: "))
    if escolha == 1:
        NomeDoProduto = input("Digite o nome do produto em questão: ")
        ValorDoProduto = float(input("Digite o valor original do produto: "))
        Quantidade = int(input("Digite quantas unidades do produto estão sendo usadas: "))
        produto = Produto(NomeDoProduto, ValorDoProduto, Quantidade)
        ValorTotal = produto.calcular_total()
        print(ValorTotal)
    
    if escolha == 2:
        print("Encerrando programa...")
        break

# Exercício 7
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
         return f"Com um {self.marca} da {self.modelo} ano {self.ano} ta bem de vida patrão!" 

MarcaDoVeiculo = input("Digite a marca do seu veículo: ")
ModeloDoVeiculo = input("Digite o modelo do sue produto: ")
AnoDoProduto = input("Digite o ano do seu vículo: ")
carro = Carro(MarcaDoVeiculo, ModeloDoVeiculo, AnoDoProduto)
print(carro.detalhes())

# Exercício 8
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self, nota1, nota2):
        media = (nota1 + nota2)/2
        if media >= 7:
            return f"O aluno {self.nome} foi aprovado com a nota: {media}!"
        
        if media < 7:
            return f"O aluno {self.nome} foi reprovado com a nota: {media}!"

while True:
    escolha = int(input("Escolha uma opção:\nDigite 1 para seguir com o programa do calculo da média do aluno.\nDigite 2 para encerrar o programa\nDigite aqui a opção escolhida: "))
    if escolha == 1:
        Nome = input("Digite o nome do aluno: ")
        PrimeiraNota = float(input("Digite a primeira do aluno: "))
        SegundaNota = float(input("Digite a segunda nota do aluno: "))
        resultado = Aluno(Nome, 0)
        MediaFinal = resultado.calcular_media(PrimeiraNota, SegundaNota)
        print(MediaFinal)    

    if escolha == 2:
        print("Encerrando programa...")
        break

# Exercício 9
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
        calculo = self.lado1 + self.lado2 + self.lado3
        return f"O valor do perímetro desse triângulo é: {calculo} cm"
    
while True:
    escolha = int(input("Escolha uma opção:\nDigite 1 para seguir com o programa do calculo do perímetro de um triângulo.\nDigite 2 para encerrar o programa\nDigite aqui a opção escolhida: "))
    if escolha == 1:
        primeiro = float(input("Digite o valor do primero lado do triângulo: "))
        segundo = float(input("Digite valor do segundo lado do triângulo: "))
        terceiro = float(input("Digite o valor do terceiro lado triâgulo: "))
        triangulo = Triangulo(primeiro, segundo, terceiro)
        perimetro = triangulo.calcular_perimetro()
        print(perimetro)

    if escolha == 2:
        print("Encerrando programa")
        break   

# Exercício 10
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Funciario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, porcentagem):
        aumento = self.salario + porcentagem
        return f"Parabéns pela promoção do funcionário {self.nome}! Seu novo cargo é {self.cargo} com o novo salário sendo R${aumento} !"

while True:
    escolha = int(input("Escolha uma opção:\nDigite 1 para seguir com o programa do calculo de aumento de salário.\nDigite 2 para encerrar o programa\nDigite aqui a opção escolhida: "))
    if escolha == 1:
        trabalhador = input("Digite o nome do funcionário: ")
        SelecaoDoCargo = int(input("Ecolha uma das opções de mudança de cargo:\n1. Estágiario para júnior\n2. Junior para Senior\n3. Senior para Responsável pelo setor\n4. Responsável do setor para Gerente\nDigite o número referente ao cargo do funcionário: "))
        if SelecaoDoCargo == 1:
            CargoEscolhido = "Estagário"
            NovoCargo = "Junior"
            ValorAtual = 1071.00
            PorcentagemDoGanho = (651/100) * ValorAtual
            funcionario = Funciario(trabalhador, ValorAtual, NovoCargo)
            NovoSalario = funcionario.aumentar_salario(PorcentagemDoGanho)
            print(f"Você foi promovido de {CargoEscolhido}. {NovoSalario}")

        if SelecaoDoCargo == 2:
            CargoEscolhido = "Junior"
            NovoCargo = "Senior"
            ValorAtual = 8041.00
            PorcentagemDoGanho = (25.5/100) * ValorAtual
            funcionario = Funciario(trabalhador, ValorAtual, NovoCargo)
            NovoSalario = funcionario.aumentar_salario(PorcentagemDoGanho)
            print(f"Você foi promovido de {CargoEscolhido}. {NovoSalario}")
        
        if SelecaoDoCargo == 3:
            CargoEscolhido = "Senior"
            NovoCargo = "Responsável pelo setor"
            ValorAtual = 10100.00
            PorcentagemDoGanho = (52/100) * ValorAtual
            funcionario = Funciario(trabalhador, ValorAtual, NovoCargo)
            NovoSalario = funcionario.aumentar_salario(PorcentagemDoGanho)
            print(f"Você foi promovido de {CargoEscolhido}. {NovoSalario}")

        if SelecaoDoCargo == 4:
            CargoEscolhido = "Responsável pelo setor"
            NovoCargo = "Gerente"
            ValorAtual = 15430.00
            PorcentagemDoGanho = (47/100) * ValorAtual
            funcionario = Funciario(trabalhador, ValorAtual, NovoCargo)
            NovoSalario = funcionario.aumentar_salario(PorcentagemDoGanho)
            print(f"Você foi promovido de {CargoEscolhido}. {NovoSalario}")

    if escolha == 2:
        print("Encerrando programa...")
        break        