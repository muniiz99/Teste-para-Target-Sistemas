# Interação com usuário.
palavra = input('Digite uma palavra: ')

# Convertendo string em uma lista de caracteres.
lista_caracteres = list(palavra)

# Invertendo a lista de caracteres.
lista_invertida = lista_caracteres[::-1]

# Juntando as letras invertidas em uma única string.
string_invertida = ''.join(lista_invertida)

# Mostrando a palavra invertida.
print('='*44)
print(string_invertida)
print('='*44)
