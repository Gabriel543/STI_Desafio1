from  alunos_csv import alunos_csv
import  email_generator
data_structure = alunos_csv()

def assign_uff_email():
    mat = input("Insira uma matricula: ")
    i = data_structure.search_matricula(mat)
    if (i >= 0):
        if (data_structure.get_aluno_by_index(i).get_status() == "Inativo"):
            print("Aluno inativo, não é possível criar um email.")
            return
        if(data_structure.get_aluno_by_index(i).get_uffmail() == '' or data_structure.get_aluno_by_index(i).get_uffmail() == 'uffmail@id.uff.br'):
            emails = email_generator.generate_email(data_structure.get_aluno_by_index(i).get_nome()).emails
            print(data_structure.get_aluno_by_index(i).get_nome() + ' escolha uma das opcoes a seguir.')
            for j in range(len(emails)):
                print(str(j + 1) + ' - ' + emails[j])
            input_value = input()
            input_value = int(input_value)
            if (input_value > 0 and input_value < len(emails)):
                data_structure.get_aluno_by_index(i).set_uffmail(emails[input_value - 1])
                print("A criação de seu email(" +emails[input_value - 1] +") será feita nos próximos minutos")
                print("Um SMS foi enviado para " + data_structure.get_aluno_by_index(i).get_telefone() + " com sua senha de acesso.")
                data_structure.update()
            else:
                print("Numero Invalido")
                return
        else:
            print("Email já existe.")
            return
    print("Matricula não existe.")

def query():
    mat = input("Insira uma matricula: ")
    i = data_structure.search_matricula(mat)
    if(i < 0):
        print("Matricula não existe.")
        return
    aluno_i = data_structure.get_aluno_by_index(i)
    print("nome: " + aluno_i.get_nome())
    print("matricula: " + aluno_i.get_matricula())
    print("telefone: " + aluno_i.get_telefone())
    print("email: " + aluno_i.get_email())
    print("uffmail: " + aluno_i.get_uffmail())
    print("status: " + aluno_i.get_status())

def activate():
    mat = input("Insira uma matricula: ")
    i = data_structure.search_matricula(mat)
    if(i < 0):
        print("Matricula não existe.")
        return
    data_structure.get_aluno_by_index(i).set_active()
    print("Aluno ativado.")

def deactivate():
    mat = input("Insira uma matricula: ")
    i = data_structure.search_matricula(mat)
    if (i < 0):
        print("Matricula não existe.")
        return
    data_structure.get_aluno_by_index(i).set_inactive()
    print("Aluno desativado.")

while (True):
    print("1: Criar um email para um usuario ativo.\n"
          "2: Consultar aluno por matricula\n"
          "3: Ativar aluno"
          "4: Desativar aluno"
          "-1: Encerrar programa")

    command = input()
    command = int(command)
    if(command == 1):
        assign_uff_email()
    elif(command == 2):
        query()
    elif(command == 3):
        activate()
    elif (command == 4):
        deactivate()
    elif(command == -1):
        print("Encerrando programa.")
        break
    else:
        print("Commando invalido")


