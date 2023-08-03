def saudacao(nome):
    print("A disciplina do semestre é " + nome)
def operacao(a, b):
    resultado = a ** b
    return resultado


saudacao("Java")

resultado_operacao = operacao(5, 3)
print(resultado_operacao)  # Saída: 8
