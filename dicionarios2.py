dicionario = {
    1: {"nome": "Maria", "idade": 26, "nacionalidade": "brasileira"}
}

print(dicionario)

dicionario.update({
    2: {"nome": "Agatha", "idade": 21, "nacionalidade": "coreana"},
    3: {"nome": "Prima Prim", "idade": 32, "nacionalidade": "tailandesa"},
    4: {"nome": "Jade", "idade": 40, "nacionalidade": "irlandesa"}
})

print(dicionario)

copia_dicionario = dicionario.copy()

dicionario.pop(2)
print(dicionario)

dicionario.popitem()
print(dicionario)

dicionario.clear()
copia_dicionario.clear()

print(dicionario)
print(copia_dicionario)


chaves = ['nome', 'idade', 'nacionalidade']
valores = ["Arthur" , 23 , 'Brasileira']
novo_dicionario = dict.fromkeys(chaves, valores)

print(novo_dicionario.items())
print(novo_dicionario.keys())
print(novo_dicionario.values())
