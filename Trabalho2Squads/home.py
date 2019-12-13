# Crie um sistema que realize a validação da regras estipuladas e apenas permita que um programador seja inserido em uma squad se estiver de acordo com seus conhecimentos de linguagem, framework e banco de dados.
# Usando as estruturas(Lista, Tuplas, Dicionarios), Classes, Metodos   
# Deve ser feito apenas no console - Usar esquema de cores.

# O programador que trabalha com Java também conhece PostgreSql. (Tiago)
# O programador que usa Angular trabalha com MongoDb. (Mateus)
# O framework de frontend de Nicole não é VUE. 
# Mateus é especialista Python e não conhece MySqlServer.
# Tiago não sabe PHP.

# Java = Tiago, Nicole
# Python = Mateus, Tiago
# PHP = Nicole

# Vue = Tiago
# Angular = Nicole, Mateus, Tiago
# React = Nicole, Tiago

# PostgreSQL = Tiago, Nicole, Mateus
# MongoDb = Mateus, Nicole, Tiago
# MySqlServer = Nicole

# Tiago = Java, Vue, PostgreSQL
# Nicole = PHP, 

import sys
sys.path.append('C:/Users/55479/Desktop/Trabalho2Squads/')
import time
from model.candidato import Candidato
from dao.candidatoDao import CandidatoDao
from dao.cores import Cores
cor = Cores()

dict_candidatos_validos = {'tiago' : ['tiago', 'java', 'vue', 'mongodb'], 'nicole' : ['nicole', 'php', 'react', 'mongodb'], 'mateus' : ['mateus', 'python', 'angular', 'postgresql']}

dict_equipes = {'padawan' : ['angular', 'mongodb'], 'labs' : ['react', 'postgresql'], 'lolita' : ['vue', 'mysqlserver']}

dict_candidato = {'nome': '', 'linguagem': '', 'framework': '', 'banco': ''}

padawan = []
labs = []
lolita = []

print('-'*20, f'{cor.verde}Menu{cor.fecha_cor} - Compatibilidade de candidatos e equipes', '-'*20)
while dict_candidatos_validos: 
    while True:
        try:
            if 'tiago' in dict_candidatos_validos:
                print('1- Tiago')
            else:
                pass

            if 'nicole' in dict_candidatos_validos:
                print('2- Nicole')
            else:
                pass

            if 'mateus' in dict_candidatos_validos:
                print('3- Mateus')
            else:
                pass

            opcao_nome = int(input(f'{cor.verde}Escolha o candidato{cor.fecha_cor}: '))
            if (opcao_nome != 1) and (opcao_nome != 2) and (opcao_nome != 3):
                raise Exception(f'Digite um {cor.vermelho}número{cor.fecha_cor} válido, conforme menu acima!')
            
            if opcao_nome == 1:
                dict_candidato['nome'] = 'tiago'
                print(f'{cor.azul}Tiago{cor.fecha_cor}\n')
            elif opcao_nome == 2:
                dict_candidato['nome'] = 'nicole'
                print(f'{cor.azul}Nicole{cor.fecha_cor}\n')
            elif opcao_nome == 3:
                dict_candidato['nome'] = 'mateus'
                print(f'{cor.azul}Mateus{cor.fecha_cor}\n')

        except Exception as erro:
            print(erro)

        else:
            break


    while True:
        try:
            opcao_linguagem = int(input(f' 1- Java\n 2- PHP\n 3- Python\n {cor.verde}Escolha a linguagem{cor.fecha_cor}: '))
            if (opcao_nome != 1) and (opcao_nome != 2) and (opcao_nome != 3):
                raise Exception(f'Digite um {cor.vermelho}número{cor.fecha_cor} válido, conforme menu acima!')

            if opcao_linguagem == 1:
                dict_candidato['linguagem'] = 'java'
                print(f'{cor.azul}Java{cor.fecha_cor}\n')
            elif opcao_linguagem == 2:
                dict_candidato['linguagem'] = 'php'
                print(f'{cor.azul}PHP{cor.fecha_cor}\n')
            elif opcao_linguagem == 3:
                dict_candidato['linguagem'] = 'python'
                print(f'{cor.azul}Python{cor.fecha_cor}\n')

        except Exception as erro:
            print(erro)

        else:
            break


    while True:
        try:
            opcao_framework = int(input(f' 1- React\n 2- Angular\n 3- Vue\n {cor.verde}Escolha o framework{cor.fecha_cor}: '))
            if (opcao_nome != 1) and (opcao_nome != 2) and (opcao_nome != 3):
                raise Exception(f'Digite um {cor.vermelho}número{cor.fecha_cor} válido, conforme menu acima!')

            if opcao_framework == 1:
                dict_candidato['framework'] = 'react'
                print(f'{cor.azul}Reac{cor.fecha_cor}\n')
            elif opcao_framework == 2:
                dict_candidato['framework'] = 'angular'
                print(f'{cor.azul}Angular{cor.fecha_cor}\n')
            elif opcao_framework == 3:
                dict_candidato['framework'] = 'vue'
                print(f'{cor.azul}Vue{cor.fecha_cor}\n')

        except Exception as erro:
            print(erro)

        else:
            break


    while True:
        try:
            opcao_banco = int(input(f' 1- MongoDb\n 2- PostgreSql\n 3- MySqlServer\n {cor.verde}Escolha o banco{cor.fecha_cor}: '))
            if (opcao_nome != 1) and (opcao_nome != 2) and (opcao_nome != 3):
                raise Exception(f'Digite um {cor.vermelho}número{cor.fecha_cor} válido, conforme menu acima!')

            if opcao_banco == 1:
                dict_candidato['banco'] = 'mongodb'
                print(f'{cor.azul}MongoDb{cor.fecha_cor}\n')
            elif opcao_banco == 2:
                dict_candidato['banco'] = 'postgresql'
                print(f'{cor.azul}PostgreSql{cor.fecha_cor}\n')
            elif opcao_banco == 3:
                dict_candidato['banco'] = 'mysqlserver'
                print(f'{cor.azul}MySqlServer{cor.fecha_cor}\n')

        except Exception as erro:
            print(erro)

        else:
            break


    person = Candidato(dict_candidato)
    pessoa = CandidatoDao(dict_candidatos_validos, dict_equipes)
    print(f'{pessoa.validar_candidato(person)}\n')

    if 'Válido' in pessoa.validar_candidato(person):
        for i in range(3):
            time.sleep(1)
            print(f'{cor.cyan}Verificando equipe adequada....{cor.fecha_cor}\n')

        print(pessoa.indicar_equipe(person))
        opcao_add = input(f'{cor.verde}Em que equipe deseja adicionar o candidato{cor.fecha_cor}:\n 1- PADAWAN\n 2- LABS\n 3- LOLITA\n: ')

        if opcao_add == '1':
            if 'PADAWAN' not in pessoa.indicar_equipe(person):
                print(f'\nCandidato incompatível com equipe {cor.azul}PADAWAN{cor.fecha_cor}!\n{cor.amarelo}Reescolha as competências dos candidatos!{cor.fecha_cor}\n')

            else:
                print(f'Adicionado com sucesso na equipe {cor.amarelo}PADAWAN{cor.fecha_cor}!!\n')
                del dict_candidatos_validos[person.get_nome()]
                padawan.append(person.get_nome())

        elif opcao_add == '2':
            if 'LABS' not in pessoa.indicar_equipe(person):
                print(f'Candidato incompatível com equipe {cor.azul}LABS{cor.fecha_cor}!\n{cor.amarelo}Reescolha as competências dos candidatos!{cor.fecha_cor}\n')
            else:
                print(f'Adicionado com sucesso na equipe {cor.amarelo}LABS{cor.fecha_cor}!!\n')
                del dict_candidatos_validos[person.get_nome()]
                labs.append(person.get_nome())

        elif opcao_add == '3':
            if 'LOLITA' not in pessoa.indicar_equipe(person):
                print(f'Candidato incompatível com equipe {cor.azul}LOLITA{cor.fecha_cor}!\n{cor.amarelo}Reescolha as competências dos candidatos!{cor.fecha_cor}\n')
            else:
                print(f'Adicionado com sucesso na equipe {cor.amarelo}LOLITA{cor.fecha_cor}!!\n')
                del dict_candidatos_validos[person.get_nome()]
                lolita.append(person.get_nome())
        
        else:
            print(f'{cor.azul}Candidato incompatível com todas as equipes !!!{cor.fecha_cor}!\n{cor.amarelo}Reescolha as competências dos candidatos!{cor.fecha_cor}\n')

                
    else:
        print(f'{cor.azul}Reescolha as competências do candidato!{cor.fecha_cor}\n')

print('-'*20, f'{cor.magento}Listagem de Candidatos Cadastrados{cor.fecha_cor}', '-'*20, f'\nEquipe Padawan: {cor.verde}{padawan}{cor.fecha_cor}\nEquipe Labs: {cor.azul}{labs}{cor.fecha_cor}\nEquipe Lolita: {cor.amarelo}{lolita}{cor.azul}')
