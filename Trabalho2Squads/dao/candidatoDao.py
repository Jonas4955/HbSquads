from model.candidato import Candidato
from dao.cores import Cores
cor = Cores()

class CandidatoDao:
    def __init__(self, dict_candidatos_validos, dict_equipes):
        self.__dict_candidatos_validos = dict_candidatos_validos
        self.__dict_equipes = dict_equipes


    def validar_candidato(self, candidato:Candidato):
        if candidato.get_framework_front() in self.__dict_candidatos_validos[candidato.get_nome()] and candidato.get_banco_de_dados() in self.__dict_candidatos_validos[candidato.get_nome()]:
            validar = 'Valido'
            print(f'Candidato {cor.amarelo}{candidato.get_nome()}{cor.fecha_cor}, é válido para entrar na equipe.\nTrabalhando com a linguagem {cor.verde}{candidato.get_linguagem()}{cor.fecha_cor} e framework {cor.vermelho}{candidato.get_framework_front}{cor.fecha_cor}!')
            return validar

        elif candidato.get_framework_front() not in self.__dict_candidatos_validos[candidato.get_nome()] and candidato.get_banco_de_dados() not in self.__dict_candidatos_validos[candidato.get_nome()]:
            validar = 'Inválido'
            print(f'Candidato {candidato.get_nome()}, não esta válido')
            return validar
        else:
            validar =  'Inválido'
            return validar

    def cadastrar_na_equipe(self, candidato:Candidato):
        if candidato.get_framework_front() in self.__dict_equipes['padawan'] and candidato.get_banco_de_dados() in self.__dict_equipes['padawan']:
            equipe = 'PADAWAN'
            print(f'Equipe compatível: {cor.amarelo}PADAWAN{cor.fecha_cor}\n')
            return equipe

        if candidato.get_framework_front() in self.__dict_equipes['labs'] and candidato.get_banco_de_dados() in self.__dict_equipes['labs']:
            equipe = 'LABS'
            print(f'Equipe compatível: {cor.amarelo}LABS{cor.fecha_cor}\n')
            return equipe
        
        if candidato.get_framework_front() in self.__dict_equipes['lolita'] and candidato.get_banco_de_dados() in self.__dict_equipes['lolita']:
            equipe = 'LOLITA'
            print(f'Equipe compatível: {cor.amarelo}LOLITA{cor.fecha_cor}\n')
            return equipe

# dict_candidato = {'nome': 'tiago', 'linguagem': 'python', 'framework': 'react', 'banco': 'mongodb'}
# person = Candidato(dict_candidato)
# pessoa = CandidatoDao()
# print(person.get_nome())