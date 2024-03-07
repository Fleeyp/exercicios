string_original = input("Digite uma string: ")

string_invertida = "" #String vazia 

for i in range(len(string_original)): #uso do len para descobrir quantos caracteres tem a string
    string_invertida = string_original[i] + string_invertida  #Ao caractere na posição [i], na string original, será atribuido o caractere da string invertida

print("String invertida:", string_invertida)