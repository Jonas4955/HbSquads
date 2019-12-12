class Candidato:
    def __init__(self, dict_candidato):
        self.__nome = dict_candidato['nome']
        self.__linguagem = dict_candidato['linguagem']
        self.__framework_front = dict_candidato['framework']
        self.__banco_de_dados = dict_candidato['banco']

    def get_nome(self):
        return self.__nome

    def get_linguagem(self):
        return self.__linguagem

    def get_framework_front(self):
        return self.__framework_front

    def get_banco_de_dados(self):
        return self.__banco_de_dados

