class Aluno:
    def __init__(self, nome, turma, nota):
        self.nome = nome
        self.turma = turma
        self.nota = nota

p1 = Aluno("Anna",3, 90)
p2 = Aluno("Ygor", 3, 100)


print(p1.nome, p1.turma, p1.nota)  
print(p2.nome, p2.turma, p2.nota) 