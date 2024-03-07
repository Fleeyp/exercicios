# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2
# valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem 
# que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem
# avisando se o número informado pertence ou não a sequência.

def fibonacci(num):
    if num == 0:
        return True

    a = 0
    b = 1
    while b <= num:
        if b == num:
            return True
        temp = b
        b = a + b
        a = temp
    return False

numero_informado = int(input("Digite um número: "))

if fibonacci(numero_informado):
    print(numero_informado, "pertence à sequência")
else:
    print(numero_informado, "não pertence a sequência")


# Utilizando atribuição múltipla
    
# def fibonacci(num):
#     if num == 0
#       return True
#
#     a = 0
#     b = 1
#     while b <= num:
#         if b == num:
#             return True
#         a, b = b, a + b #atribuição múltipla
#     return False

# numero_informado = int(input("Digite um número: "))

# if fibonacci(numero_informado):
#     print(numero_informado, "pertence à sequência")
# else:
#     print(numero_informado, "não pertence a sequência")