#Amplie a classe Aluno com um método exibir_dados() que imprime nome, matrícula e curso.

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

p1 = Aluno("Anna",3109, "Desenvolvimento de Sistemas")
p2 = Aluno("Ygor", 1510, " Controle e Processos Industriais")


exibir_dados =(print(p1.nome, p1.matricula, p1.curso)  )
(print(p2.nome, p2.matricula, p2.curso)  )

