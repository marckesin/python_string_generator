import string
import random

def string_g(tamanho=8, letras=string.ascii_letters + string.digits + string.punctuation):
    resultado = [random.choice(letras) for i in range(tamanho)]
    resultado = ''.join(resultado)
    if len(resultado) == tamanho:
        return resultado

def new_word(text='exemplo'):
	palavra = []
	dic = {
	'a' : '4',
	'b' : '8',
	'e' : '3',
	'g' : '6',
	'i' : '1',
	'o' : '0',
	'p' : '9',
	's' : '5',
	't' : '7',
	'z' : '2'
	}

	for letra in text:
		if letra.lower() in dic:
			letra = dic[letra.lower()]
		palavra.append(letra)
	palavra = ''.join(palavra)
	return palavra

def all_combinations(palavra='exemplo'):
	tamanho = 2**(len(palavra)) # especifica a quantidade de combinações possíveis
	unicos = set()

	for i in range(tamanho):
		texto = []
		binario = format(i, str('0%db' % len(palavra))) # cria um numero binario com o mesmo comprimento da palavra
		
		for b in range(len(binario)):
			if binario[b] == '0':
				texto.append(palavra[b].lower())
			else:
				texto.append(palavra[b].upper())
		unicos.add(''.join(texto))

	lista = sorted(unicos)
	return lista
