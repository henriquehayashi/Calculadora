# Versão 2.0 - 15/05/2026
# Atualização: mudanças no código da calculadora - funções, dicionário, criação de interface

import math

# Funções
def soma(a, b):
    return a + b

def subtração(a, b):
    return a - b

def multiplicação(a, b):
    return a * b

def divisão(a, b):
    if b == 0:
       return "Erro: valor indefinido"
    else:
        return a / b
    
def porcentagem(a, b):
    return a / 100 * b

def seno(a):
    return math.sin(math.radians(a))

def cosseno(a):
    return math.cos(math.radians(a))

def tangente(a):
    if a == 90 or a == 270:
        return "Erro: valor indefinido"
    x = math.tan(math.radians(a))
    if abs(x) < 1e-10:
        x = 0
    return x
    
def radiciação(a):
    if a < 0:
        return "Erro: solução não real"
    x = math.sqrt(a)
    return x

# Dicionário
operações = {
    "1": soma,
    "2": subtração,
    "3": multiplicação,
    "4": divisão,
    "5": porcentagem,
    "6": seno,
    "7": cosseno,
    "8": tangente,
    "9": radiciação
}

def execucao():
    print("Seja bem vindo! Escolha sua operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Porcentagem")
    print("6 - Seno")
    print("7 - Cosseno")
    print("8 - Tangente")
    print("9 - Radiciação")
    op = input("Opção: ")

    if op in operações:
        if op in ["1", "2", "3", "4", "5"]:
            a = float(input("Primeiro número: "))
            b = float(input("Segundo número: "))
            resultado = operações[op](a,b)
        else:
            a = float(input("Único número: "))
            resultado = operações[op](a)

        return resultado
    else:
        return "Operação inválida"

resultado = execucao()
print(f"Resultado: {resultado}")

while True:
    repeat = input("Deseja realizar outra operação?(s/n)")
    if repeat.lower() != "s":
        print("Até a próxima!")
        break
    resultado = execucao()
    print(f"Resultado: {resultado}")