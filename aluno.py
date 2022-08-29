from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self,nome,matricula,telefone,email,uffmail,status):
        super(Aluno, self).__init__(nome,email,telefone)
        self.__matricula = matricula
        self.__uffmail = uffmail
        self.__status = status

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self,matricula):
        self.__matricula = matricula

    def get_uffmail(self):
        return self.__uffmail

    def set_uffmail(self,uffmail):
        self.__uffmail = uffmail

    def get_status(self):
        return self.__status

    def set_active(self):
        self.__status = "Ativo"

    def set_inactive(self):
        self.__status = "Inativo"

