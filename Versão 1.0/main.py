# Versão 1.0 - 20/04/2026
# Calculadora simples com operações básicas, funções trigonométricas,
# raiz quadrada e porcentagem.

import math

num1 = float(input(" "))
sinal = input(" ")
if sinal == "sqrt" or sinal == "sin" or sinal == "cos" or sinal == "tan":
    num2 = 0
else: num2 = float(input(" "))
resultado = (num1 + num2) if sinal == "+" else (num1 - num2) if sinal == "-" else (num1 * num2) if sinal == "*" else (num1 / num2) if sinal == "/" else (num1 ** num2) if sinal == "**" else (math.sqrt(num1)) if sinal == "sqrt" else "Sinal inválido"
resultado = math.sin(math.radians(num1)) if sinal == "sin" else math.cos(math.radians(num1)) if sinal == "cos" else math.tan(math.radians(num1)) if sinal == "tan" else resultado
resultado = ("Erro: Divisão por zero.") if sinal == "/" and num2 == 0 else resultado
resultado = ("Erro: Solução não real.") if sinal == "sqrt" and num1 < 0 else resultado
resultado = ("Valor indefinido (tan = sen/cos ; cos = 0).") if sinal == "tan" and (num1 == 90 or num1 == 270) else resultado
resultado = (num1/100 * num2) if sinal == "%" else resultado

print(f"{resultado}")

while True:
    repeat = input("Deseja realizar outra operação? (s/n) ")
    if repeat.lower() == "s":
        repeat_num1 = float(input(" "))
        repeat_sinal = input(" ")
        if repeat_sinal == "sqrt" or repeat_sinal == "sin" or repeat_sinal == "cos" or repeat_sinal == "tan":
            repeat_num2 = 0
        else: repeat_num2 = float(input(" "))
        repeat_resultado = (repeat_num1 + repeat_num2) if repeat_sinal == "+" else (repeat_num1 - repeat_num2) if repeat_sinal == "-" else (repeat_num1 * repeat_num2) if repeat_sinal == "*" else (repeat_num1 / repeat_num2) if repeat_sinal == "/" else (repeat_num1 ** repeat_num2) if repeat_sinal == "**" else (math.sqrt(repeat_num1)) if repeat_sinal == "sqrt" else "Sinal inválido"
        repeat_resultado = math.sin(math.radians(repeat_num1)) if repeat_sinal  == "sin" else math.cos(math.radians(repeat_num1)) if repeat_sinal == "cos" else math.tan(math.radians(repeat_num1)) if repeat_sinal == "tan" else repeat_resultado
        repeat_resultado = ("Erro: Divisão por zero.") if repeat_sinal == "/" and repeat_num2 == 0 else repeat_resultado
        repeat_resultado = ("Erro: Solução não real.") if repeat_sinal == "sqrt" and repeat_num1 < 0 else repeat_resultado
        repeat_resultado = ("Valor indefinido (tan = sen/cos ; cos = 0).") if repeat_sinal == "tan" and (repeat_num1 == 90 or repeat_num1 == 270) else repeat_resultado
        repeat_resultado = (repeat_num1/100 * repeat_num2) if repeat_sinal == "%" else repeat_resultado

        print(f"{repeat_resultado}")
    else:
        break