meu_dicionario = {
    1: "Python",
    2: "Java",
    3: "PHP"
}

print(meu_dicionario)
print(type(meu_dicionario))
print(meu_dicionario.get("linguagem"))

print(len(meu_dicionario))

dicionario_frutas = dict({
    1: dict(nome="limão", tipo="ácida"),
    2: dict(nome="laranja", tipo="ácida"),
    3: dict(nome="manga", tipo="semiácida"),
    4: dict(nome="maçã", tipo="semiácida"),
    5: dict(nome="banana", tipo="doce"),
    6: dict(nome="mamão", tipo="doce")
})

print(f"Nome: {dicionario_frutas[1]['nome']}, Tipo: {dicionario_frutas[1]['tipo']}")

print(f"Nome: {dicionario_frutas[2]['nome']}, Tipo: {dicionario_frutas[2]['tipo']}")

for chave, valores in dicionario_frutas.items():
    print(f"Chave {chave} - Nome: {valores['nome']}, Tipo: {valores['tipo']}")