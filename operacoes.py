
def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_reprovacao(media):
    return media < 6

def exibir_reprovados(dados_alunos, matriculas_reprovados):

    resultado = []
    for matricula in matriculas_reprovados:
        aluno = dados_alunos.get(matricula)
        if aluno:
            nome = aluno['nome']
            media = aluno['media']
            resultado.append(f'Aluno Reprovado: {nome} – Matrícula: {matricula} – Média Final: {media:.2f}')
    return '\n'.join(resultado)