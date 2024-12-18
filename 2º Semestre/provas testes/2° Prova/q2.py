class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

class Curso:
    def __init__(self, nome_do_curso):
        self.nome_do_curso = nome_do_curso
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

curso = Curso("Engenharia de Software")
aluno1 = Aluno("Ana", "001")
aluno2 = Aluno("Pedro", "002")

curso.adicionar_aluno(aluno1)
curso.adicionar_aluno(aluno2)

for aluno in curso.alunos:
    print(f"Aluno: {aluno.nome}, Matrícula: {aluno.matricula}")
