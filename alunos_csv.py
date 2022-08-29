import csv
import aluno

class alunos_csv:
    def load(self):
        alunos = []
        with open("alunos.csv", 'r') as file:
            csv_reader = csv.DictReader(file)
            for line in csv_reader:
                temp_aluno = aluno.Aluno(line['nome'], line['matricula'], line['telefone'], line['email'],
                                         line['uffmail'], line['status'])
                alunos.append(temp_aluno)
        return alunos
    def __init__(self):
        self.__alunos = self.load()

    def search_matricula(self,matricula):
        i = 0
        for l in self.__alunos:
            if(l.get_matricula() == matricula):
                return i
            i+=1
        return -1

    def update(self):
        with open("alunos.csv", 'w',newline='') as file:
            field_names = ['nome','matricula','telefone','email','uffmail','status']
            csv_writer = csv.DictWriter(file,fieldnames=field_names)
            csv_writer.writeheader()
            for l in self.__alunos:
                csv_writer.writerow({'nome': l.get_nome(),'matricula': l.get_matricula(),'telefone': l.get_telefone(),'email':l.get_email(),'uffmail':l.get_uffmail(),'status':l.get_status()})

    def get_aluno_by_index(self,i):
        return self.__alunos[i]




