from model.candidato import Candidato
from dao.cores import Cores
cor = Cores()

class CandidatoDao:
    def __init__(self, dict_candidatos_validos, dict_equipes):
        self.__dict_candidatos_validos = dict_candidatos_validos
        self.__dict_equipes = dict_equipes


    def validar_candidato(self, candidato:Candidato):
        if (candidato.get_framework_front() in self.__dict_candidatos_validos[candidato.get_nome()]) or (candidato.get_banco_de_dados() in self.__dict_candidatos_validos[candidato.get_nome()]):
            return f'Candidato {cor.amarelo}{candidato.get_nome()}{cor.fecha_cor}, é Válido para entrar na equipe.\nTrabalhando com a linguagem {cor.verde}{candidato.get_linguagem()}{cor.fecha_cor} e framework {cor.vermelho}{candidato.get_framework_front()}{cor.fecha_cor}!'

        elif (candidato.get_framework_front() not in self.__dict_candidatos_validos[candidato.get_nome()]) or (candidato.get_banco_de_dados() not in self.__dict_candidatos_validos[candidato.get_nome()]):
            return f'Candidato {cor.amarelo}{candidato.get_nome()}{cor.fecha_cor}, esta Inválido.'

        else:
            return f'Candidato {cor.amarelo}{candidato.get_nome()}{cor.fecha_cor}, esta Inválido.'


    def indicar_equipe(self, candidato:Candidato):
        padawan = ''
        labs = ''
        lolita = ''
        if candidato.get_framework_front() in self.__dict_equipes['padawan'] or candidato.get_banco_de_dados() in self.__dict_equipes['padawan']:
            padawan = 'PADAWAN'
            print(f'Equipe compatível: {cor.amarelo}PADAWAN{cor.fecha_cor}\n')

        if candidato.get_framework_front() in self.__dict_equipes['labs'] or candidato.get_banco_de_dados() in self.__dict_equipes['labs']:
            labs = 'LABS'
            print(f'Equipe compatível: {cor.amarelo}LABS{cor.fecha_cor}\n')
        
        if candidato.get_framework_front() in self.__dict_equipes['lolita'] or candidato.get_banco_de_dados() in self.__dict_equipes['lolita']:
            lolita = 'LOLITA'
            print(f'Equipe compatível: {cor.amarelo}LOLITA{cor.fecha_cor}\n')

        return padawan + labs + lolita
        
