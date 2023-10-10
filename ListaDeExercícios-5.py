# Exercício 1

class FilaDeImpressao:
    def __init__(self):
        self.fila = []

    def adicionar_documento(self, documento):
        self.fila.append(documento)

    def imprimir_documentos(self):
        while self.fila:
            documento = self.fila.pop(0)
            print(f'Imprimindo documento: {documento}')

# Exercício 2

class FilaDeAtendimento:
    def __init__(self):
        self.fila = []

    def adicionar_cliente(self, cliente):
        self.fila.append(cliente)

    def atender_clientes(self):
        while self.fila:
            cliente = self.fila.pop(0)
            print(f'Atendendo o cliente: {cliente}')


# Exercício 3

class GerenciamentoDePedidos:
    def __init__(self):
        self.fila_pedidos = []

    def adicionar_pedido(self, pedido):
        self.fila_pedidos.append(pedido)

    def processar_pedidos(self):
        while self.fila_pedidos:
            pedido = self.fila_pedidos.pop(0)
            print(f'Processando pedido: {pedido}')


# Exercício 4

class ListaDeTarefas:
    def __init__(self):
        self.fila_tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.fila_tarefas.append(tarefa)

    def concluir_tarefas(self):
        while self.fila_tarefas:
            tarefa = self.fila_tarefas.pop(0)
            print(f'Concluindo tarefa: {tarefa}')


# Exercício 5

class FilaDePedidosOnline:
    def __init__(self):
        self.fila_pedidos = []

    def adicionar_pedido(self, pedido):
        self.fila_pedidos.append(pedido)

    def processar_pedidos(self):
        while self.fila_pedidos:
            pedido = self.fila_pedidos.pop(0)
            print(f'Processando pedido online: {pedido}')


# Exercício 6

class NavegadorWeb:
    def __init__(self):
        self.historico = []
        self.indice_atual = -1

    def visitar_pagina(self, pagina):
        if self.indice_atual < len(self.historico) - 1:
            self.historico = self.historico[:self.indice_atual + 1]
        self.historico.append(pagina)
        self.indice_atual += 1

    def voltar(self):
        if self.indice_atual > 0:
            self.indice_atual -= 1

    def avancar(self):
        if self.indice_atual < len(self.historico) - 1:
            self.indice_atual += 1


# Exercício 7

class CalculadoraRPN:
    def __init__(self):
        self.pilha = []

    def avaliar_rpn(self, expressao):
        tokens = expressao.split()
        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                self.pilha.append(int(token))
            elif token in ['+', '-', '*', '/']:
                b = self.pilha.pop()
                a = self.pilha.pop()
                if token == '+':
                    self.pilha.append(a + b)
                elif token == '-':
                    self.pilha.append(a - b)
                elif token == '*':
                    self.pilha.append(a * b)
                elif token == '/':
                    self.pilha.append(a / b)
        return self.pilha[0]


# Exercício 8

class EditorDeTexto:
    def __init__(self):
        self.hist_comandos = []
        self.indice_atual = -1

    def executar_comando(self, comando):
        if self.indice_atual < len(self.hist_comandos) - 1:
            self.hist_comandos = self.hist_comandos[:self.indice_atual + 1]
        self.hist_comandos.append(comando)
        self.indice_atual += 1

    def desfazer(self):
        if self.indice_atual > 0:
            self.indice_atual -= 1

    def refazer(self):
        if self.indice_atual < len(self.hist_comandos) - 1:
            self.indice_atual += 1


# Exercício 9

def encontrar_operadores(expression):
    operadores = set()
    for char in expression:
        if char in ['+', '-', '*', '/', '(', ')', '^']:
            operadores.add(char)
    return operadores


# Exercício 10

def e_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    pilha = []
    for char in palavra:
        pilha.append(char)
    reverso = ''.join(pilha[::-1])
    return palavra == reverso

print(e_palindromo("radar"))
print(e_palindromo("python"))
