'''Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.'''


def ex2(valor):
# Declarando 2 variáveis com os valores iniciar da senquência de fibonacci.
    n1, n2 = 0, 1
# Lógica para descobrir se o valor informado pertence a sequência de fibonacci.
    while n2 < valor:
        n1, n2 = n2, n1 + n2
    if n2 == valor:
        return True
    else:
        return False

#Interação com usuário para saber se o valor informado pertence a sequência de fibonacci.
valor = int(input("Digite um número: "))
print('='*44)
if ex2(valor):
    print(f"{valor} pertence à sequência de Fibonacci.")
else:
    print(f"{valor} não pertence à sequência de Fibonacci.")
print('='*44)