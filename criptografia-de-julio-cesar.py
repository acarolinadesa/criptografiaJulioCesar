# -*- coding: utf-8 -*-
import sys
import json
import hashlib
import requests

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

#Acessar Json e pegar dados mensagem cifrada e numero de casas 
with open('answer.json', 'r') as answer: 
    dados = json.loads(answer.read())
    mensagemCifrada = dados['cifrado']
    ROT = dados['numero_casas']

#------------------funcoes-----------------------------
def decifraMensagem(mensagemCifrada):
        mensagemDecifrada = ''
        for letra in mensagemCifrada:
            if letra in ALPHABET:
                letra_index = ALPHABET.index(letra) #esse indice foi criado para descobrir a letra do alfabeto
                mensagemDecifrada += ALPHABET[(letra_index - ROT)% len(ALPHABET)] 
                #%len(ALPHABET) para passar das letras finais do alfabeto para as letras do inicio
            else:
                mensagemDecifrada += letra
        return mensagemDecifrada

def main():
    decifraMensagem(mensagemCifrada)

#Enviar mensagem decifrada para o Json
with open('answer.json', 'r') as answer:
    dados=json.load(answer)

mensagemDecifrada = decifraMensagem(mensagemCifrada)
dados['decifrado'] = mensagemDecifrada

with open('answer.json', 'w') as answer:
    json.dump(dados, answer)

#-------------funcao principal (main)------------------
if __name__ == "__main__":
    main()



#Criptografia SHA1 com Python para criar resumo criptografico do texto decifado 
#Conferi no https://www.browserling.com/tools/all-hashes e está correto o/
with open('answer.json', 'r') as answer: 
    dados = json.load(answer)

resumo = hashlib.sha1(dados['decifrado']).hexdigest()
dados['resumo_criptografico'] = resumo

with open('answer.json', 'w') as answer:
    json.dump(dados, answer)

#Submentendo arquivo answer.json via POST para a API
#Arquivo answer.json foi submetido no Postman