class Aluno:
    def __init__(self, matricula, sexo, nome, idade):
        self.matricula = matricula
        self.sexo = sexo 
        self.nome = nome 
        self.idade = idade

if __name__ == "__main__":
    aluno1 = Aluno("756756757", "F", "Giovanna", 17)
    aluno2 = Aluno("543876578", "M", "Fernando", 18)
    print(aluno1.matricula, aluno1.sexo, aluno1.nome, aluno1.idade)
    print(aluno2.matricula, aluno2.sexo, aluno2.nome, aluno2.idade)