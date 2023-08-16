#  Exercício 1:
# ------------------------------------------------------------------------------------------------------------------------------------------------

while True: 
  print("Digite abaixo três números para que deles seja feita uma média: ") 
  N1 = float(input("Digite o primeiro número: "))
  N2 = float(input("Digite o segundo número: "))
  N3 = float(input("Digite o terciro número: "))
  Me = (N1 + N2 + N3)/3 
  print(f"A média dos números digitados anteriormente é: {Me}") 
  Repetir = int(input("Se dseja repetir o programa digite: 1 \nSe não deseja repetir o programa digite: 2\n")) 
  if Repetir == 2:
   break
 
#  Exercício 2:
# ------------------------------------------------------------------------------------------------------------------------------------------------

while True:
   N = int(input("Digite um número para saber se é ímpar ou par: "))
   if N % 2 == 0:
    print("O número digitado é par!")
   else:
    print("O número digitado é ímpar!")
   Repetir = int(input("Se deseja repetir o programa digite: 1\nSe não deseja repetir o programa digite: 2\n"))
   if Repetir == 2:
    break
 
 # Exercício 3:
# ------------------------------------------------------------------------------------------------------------------------------------------------

while True:
    print("O progama dará todos os números pares até um número escolhido")
    N = int(input("Digite o número escolhido a operação: "))
    NumeroPar = []
    for numero in range(0, N + 1, 2):
     NumeroPar.append(numero)
     print(f"Os números pares até o número escolhido são: {NumeroPar}") 
    Repetir = int(input("Se deseja repetir o programa digite: 1\nSe não deseja repetir o programa digite: 2\n"))
    if Repetir == 2:
      break

# Exercício 4:
# ------------------------------------------------------------------------------------------------------------------------------------------------

Numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
NumerosPares = []
for par in Numeros:
    if par % 2 == 0:
     NumerosPares.append(par)
     print(f"Os númros pares dessa lista são: {NumerosPares}")

# Exrcício 5:
# ------------------------------------------------------------------------------------------------------------------------------------------------

Numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
QuantidadeDePares = 0
NumerosPares = []
SomaDosPares = 0
for par in Numeros:
    if par % 2 == 0:
     NumerosPares.append(par)
     QuantidadeDePares += 1
     SomaDosPares += par
     MediaDePares = SomaDosPares/QuantidadeDePares
     print(f"A média dos números pares dentro dessa lista é(contando o 0 como número par): {MediaDePares}")

# Exercício 6:
# ------------------------------------------------------------------------------------------------------------------------------------------------

while True:
    Fatorial = int(input("Digite um número inteiro e positivo para que seja feito o calculo de seu fatorial: "))
    Resultado = 1
    for fatores in range(1, Fatorial+1):
        Resultado *= fatores
        print(f"O Fatorial do número digitado é: {Resultado}")
    Repetir = int(input("Se deseja repetir o programa digite: 1\nSe não deseja repetir o programa digite: 2\n"))
    if Repetir == 2:
       break

# Exercício 7:
# ------------------------------------------------------------------------------------------------------------------------------------------------

def SequenciaDeFibonnaci(x):
    Sequencia = [0, 1]
    while Sequencia[-1] + Sequencia[-2] <= x:
        NumeroSequinte = Sequencia[-1] + Sequencia[-2]
        Sequencia.append(NumeroSequinte)
    return Sequencia

while True:
    NumeroFinal = int(input("Digite o número que será o último em uma sequência de Fibonnaci para que seja dado uma lista com todos os números dentro dessa sequência: "))
    ListaDaSequencia = SequenciaDeFibonnaci(NumeroFinal)
    print(f"O último número da sequência de Fibonnaci até valor dado séria: {ListaDaSequencia}")
    Repetir = int(input("Se deseja repetir o programa digite: 1\nSe não deseja repetir o programa digite: 2\n"))
    if Repetir == 2:
        break

# Exercicio 8:
# ------------------------------------------------------------------------------------------------------------------------------------------------

def Primo(Numero):
    for x in range(2, int(Numero**0.5) + 1):
        if Numero % x == 0:
            return False
    return True
while True:
    Numero = int(input("Digite um número paar saber se ele é primo ou não: "))
    if Primo(Numero):    
        print(f"O número {Numero} é primo")
    else:
        print(f"O número {Numero} não é primo")
    Repetir = int(input("Se deseja repetir o programa digite: 1\nSe não deseja repetir o programa digite: 2\n"))
    if Repetir == 2:
        break    

# Exercício 9
# ------------------------------------------------------------------------------------------------------------------------------------------------

Nomes = ["alan", "joana", "douglas", "ana","vitor" ]
PrimeiraLetra = "a"
for string in Nomes:
   if string[0] == PrimeiraLetra:
     print(string)

# Exercício 10
# ------------------------------------------------------------------------------------------------------------------------------------------------

import random
while True:
    print(f"Bem vindo ao jokenpo\nQual será sua escolha?\n1. Pedra\n2. Papel\n3. Tesoura")
    Maquina = (1, 2, 3) 
    EscolhaUsr = int(input("Digite o número 4 caso queira sair do jogo\nDigite aqui o número referente a sua escolha:"))
    if EscolhaUsr == 4:
        break
    if EscolhaUsr not in (1, 2, 3):
        print("Escolha apenas das opções 1 a 4!!!\n\n")
        continue 
    EscolhaMaquina = random.choice(Maquina)    
    if EscolhaUsr == 1:
        if EscolhaMaquina == 1:
            print("A escolha do seu oponene foi PEDRA !!!\nO JOGO EMPATOU !!!\n\n")
        if EscolhaMaquina == 2:
            print("A escolha do seu oponente foi PAPEL !!!\nVOCÊ PERDEU !!!\n\n")
        if EscolhaMaquina == 3:
            print("A escolha do seu oponente foi Tesoura !!!\nVOCÊ GANHOU !!!\n\n")
    if EscolhaUsr == 2:
        if EscolhaMaquina == 1:
            print("A escolha do seu oponene foi PEDRA !!!\nVOCÊ GANHOU !!!\n\n")
        if EscolhaMaquina == 2:
            print("A escolha do seu oponente foi PAPEL !!!\nO JOGO EMPATOU !!!\n\n")
        if EscolhaMaquina == 3:
            print("A escolha do seu oponente foi Tesoura !!!\nVOCÊ PERDEU !!!\n\n")
    if EscolhaUsr == 3:
        if EscolhaMaquina == 1:
            print("A escolha do seu oponene foi PEDRA !!!\nVOCÊ PERDEU !!!\n\n")
        if EscolhaMaquina == 2:
            print("A escolha do seu oponente foi PAPEL !!!\nVOCÊ GANHOU !!!\n\n")
        if EscolhaMaquina == 3:
            print("A escolha do seu oponente foi Tesoura !!!\nO JOGO EMPATOU !!!\n\n")