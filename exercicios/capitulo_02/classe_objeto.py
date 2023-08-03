class estudo():
    def __init__(self, disciplina, carga_horaria, diploma):
        self.disciplina = disciplina
        self.carga_horaria = carga_horaria
        self.tem_diploma = diploma

    def curso(self):
        print("A disciplina do semestre é " + self.disciplina)

    def concluida(self):
        print("A carga horarida da disciplina " + self.disciplina + " é " + self.carga_horaria)

    def diploma(self):
        if self.tem_diploma:
            print(
                "O diploma da disciplina " + self.disciplina + "esta disponivel com a carga horaria " + self.carga_horaria)
        else:
            print("Não conseguiu diploma")


python = estudo("Python", "1600h", True)
java = estudo("Java", "3600h", True)
node = estudo("NodeJs", "1000h", False)
node.curso()
node.concluida()
node.diploma()

python.curso()
python.concluida()
python.diploma()

java.curso()
java.concluida()
java.diploma()
