# Descubra a lógica e complete o próximo elemento:

# a) 1, 3, 5, 7, ___
# b) 2, 4, 8, 16, 32, 64, ____
# c) 0, 1, 4, 9, 16, 25, 36, ____
# d) 4, 16, 36, 64, ____
# e) 1, 1, 2, 3, 5, 8, ____
# f) 2,10, 12, 16, 17, 18, 19, ____

# a) O próximo número será 9, pois se trata de uma sequência de 2 em 2

#Raciocínio em código:

# ultimo_numero = 7
# proximo_numero = ultimo_numero + 2
# print(proximo_numero)

# b) O próximo número será 128, pois se trata de uma sequência de potências de 2, ou consequentemente, o anterior multiplicado por 2,

#Raciocínio em código:

# ultimo_numero = 64
# proximo_numero = ultimo_numero * 2
# print(proximo_numero)

# c) O próximo número será 49, pois se trata da sequência dos números inteiros elevados a 2.

#Raciocínio em código: Levando em conta que o item na posição 0 assume índice 1.

# indice_ultimo_numero = 6
# proximo_numero = (indice_ultimo_numero + 1) ** 2

# print(proximo_numero)

# d) O próximo número será 100, pois se trata da sequência dos números pares elevados a 2.

#Raciocínio em código: 

# ultimo_numero = 8 ** 2
# proximo_numero = (8 + 2) ** 2

# print(proximo_numero)

# e) O próximo número será 13, pois se trata da sequência de Fibonacci, cujo próximo número é a soma dos 2 anteriores (8 e 5)

# f) O próximo número será 200, pois é o próximo número cujo nome começa com a letra "D" (essa foi sacanagem ein...)

