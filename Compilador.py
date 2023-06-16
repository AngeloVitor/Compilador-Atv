def transformar_glc_para_fng(glc):
    fng = glc.copy()

    # Passo 1: Remover recursão à esquerda direta
    for nao_terminal in fng:
        producoes = fng[nao_terminal]
        substituicoes = [producao for producao in producoes if producao and producao[0] == nao_terminal]
        for substituicao in substituicoes:
            producoes.remove(substituicao)
            for nova_producao in fng[substituicao[1]]:
                producoes.append(nova_producao + substituicao[2:])
        if substituicoes:
            print("Passo 1: Removida recursão à esquerda direta para o não-terminal", nao_terminal)

    # Passo 2: Introduzir não terminais auxiliares
    novo_nao_terminal = "Z"
    while novo_nao_terminal in fng:
        novo_nao_terminal += "'"

    for nao_terminal in fng:
        producoes = fng[nao_terminal]
        substituicoes = []
        for producao in producoes:
            if producao and producao[0] == nao_terminal:
                substituicoes.append(producao[1:] + novo_nao_terminal)
                producoes.remove(producao)

        if substituicoes:
            fng[novo_nao_terminal] = substituicoes
            producoes.append(novo_nao_terminal)
            print("Passo 2: Introduzido não-terminal auxiliar", novo_nao_terminal, "para o não-terminal", nao_terminal)
            novo_nao_terminal = chr(ord(novo_nao_terminal) + 1)  # Incrementar o próximo não-terminal auxiliar

    # Passo 3: Remover produções unitárias
    for nao_terminal in fng:
        producoes = fng[nao_terminal]
        substituicoes = [producao for producao in producoes if len(producao) == 1 and producao in fng]
        for substituicao in substituicoes:
            producoes.remove(substituicao)
            producoes += fng[substituicao]
        if substituicoes:
            print("Passo 3: Removida produção unitária para o não-terminal", nao_terminal)

    # Passo 4: Renomear não terminais
    novo_nome = "S"
    while novo_nome in fng:
        novo_nome += "'"

    fng[novo_nome] = fng.pop("S")
    print("Passo 4: Renomeado símbolo inicial para", novo_nome)

    return fng


# Exemplo de GLC
# o "v" foi colocado para simbolizar a lambda, porque o simbolo da lambda não pega quando o código vai rodar
glc = {
    "S": ["aAd", "A"],
    "A": ["Bc", "V"],
    "B": ["Ac", "a"]
}

fng = transformar_glc_para_fng(glc)

print("\nGramática resultante na Forma Normal de Greibach (FNG):")
for nao_terminal in fng:
    for producao in fng[nao_terminal]:
        print(nao_terminal, "->", producao)