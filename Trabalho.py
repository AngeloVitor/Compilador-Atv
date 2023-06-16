import re


def valida_caracteres(string):
    # Verifica se a string contém apenas caracteres válidos
    padrao = r"[^a-zA-Z0-9]"
    if re.search(padrao, string):
        return False
    else:
        return True


def valida_palavra(palavra):
    # Verifica se a palavra começa com consoante e alterna corretamente entre consoantes e vogais
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vogais = "aeiouAEIOU"
    if palavra[0] not in consoantes:
        return False
    for i in range(1, len(palavra)):
        if (palavra[i-1] in consoantes and palavra[i] in consoantes) or \
           (palavra[i-1] in vogais and palavra[i] in vogais):
            return False
    return True


def analisador_lexico(string):
    # Divide a string em palavras e verifica cada uma
    tokens = string.split()
    for token in tokens:
        if len(token) > 10:
            token = token[:10]
            print(f"A string é válida: Porem o token '{token}' excede o limite máximo de 10 caracteres.")
            return
        if not valida_caracteres(token):
            print(f"A string é inválida: O token '{token}' contém caracteres inválidos.")
            return
        if token[0] in "zx":
            print(f"A string é inválida: O token '{token}' é uma palavra reservada.")
            return
        if token[0] in "jwkyçhqJWKYÇHQ":
            print(f"A string é inválida: O token '{token}' é uma palavra não reservada.")
            return
        if token[-1] in "0123456789":
            palavra = token[:-1]
            if any(c.isdigit() for c in palavra):
                print(f"A string é inválida: A palavra '{token}' contém numeral.")
                return
        else:
            palavra = token
            if any(c.isdigit() for c in palavra):
                print(f"A string é inválida: A palavra '{token}' contém numeral.")
                return
        if not valida_palavra(palavra):
            print(f"A string é inválida: O token '{token}' não alterna corretamente entre consoantes e vogais.")
            return
    print("A string é válida.")

parador = ""
# Exemplo de uso:
while parador != "parar":
    analisador_lexico(input("Analisador lexico: "))
    print("Deseja parar?(Digite parar) ")
    parador = input("")

#analisador_lexico("Oi Pess0@l!")
#analisador_lexico("gAbCdeFgHi")
#analisador_lexico("Exemplo 12345")
#analisador_lexico("Munomunomuno")
#analisador_lexico("T3st3 V4l1d0")
#analisador_lexico("abcde")
#analisador_lexico("1234567890")
#analisador_lexico("banana2323")
#analisador_lexico("Testando 123")
#analisador_lexico("Este é um exemplo de string válida.")