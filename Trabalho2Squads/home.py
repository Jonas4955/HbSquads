# Crie um sistema que realize a validação da regras estipuladas e apenas permita que um programador seja inserido em uma squad se estiver de acordo com seus conhecimentos de linguagem, framework e banco de dados.
# Usando as estruturas(Lista, Tuplas, Dicionarios), Classes, Metodos   
# Deve ser feito apenas no console - Usar esquema de cores.

# - Bancos de dados no ambiente HBSIS, o MySqlServer, PostgreSQL e o MongoDb.
# - Linguagem de backend,  Python, Java e PHP.
# - Framework de frontend estão sendo utilizados o React, Angular e Vue.
# - Várias squads que utilizam a mesma linguagem de backend porém utilizam banco de dados e framework frontend distintos.
# - Foi realizada uma avaliação com cada um dos programadores Mateus, Tiago e a Nicole. 

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


opcao_nome = int(input(' 1- Tiago\n 2- Nicole\n 3- Mateus\n Escolha o candidato:\n'))

if opcao_nome == 1:
    dict_candidato['nome'] = 'tiago'
    print('Tiago\n')
elif opcao_nome == 2:
    dict_candidato['nome'] = 'nicole'
    print('Nicole\n')
elif opcao_nome == 3:
    dict_candidato['nome'] = 'mateus'
    print('Mateus\n')

opcao_linguagem = int(input(' 1- Java\n 2- PHP\n 3- Python\n Escolha a linguagem:\n'))

if opcao_linguagem == 1:
    dict_candidato['linguagem'] = 'java'
    print('Java\n')
elif opcao_linguagem == 2:
    dict_candidato['linguagem'] = 'php'
    print('PHP\n')
elif opcao_linguagem == 3:
    dict_candidato['linguagem'] = 'python'
    print('Python\n')

opcao_framework = int(input(' 1- React\n 2- Angular\n 3- Vue\n Escolha o framework:\n'))

if opcao_linguagem == 1:
    dict_candidato['framework'] = 'react'
    print('Reac\n')
elif opcao_linguagem == 2:
    dict_candidato['framework'] = 'angular'
    print('Angular\n')
elif opcao_linguagem == 3:
    dict_candidato['framework'] = 'vue'
    print('Vue\n')

opcao_banco = int(input(' 1- MongoDb\n 2- PostgreSql\n 3- MySqlServer\n Escolha o banco:\n'))

if opcao_banco == 1:
    dict_candidato['banco'] = 'mongodb'
    print('MongoDb')
elif opcao_banco == 2:
    dict_candidato['banco'] = 'postgresql'
    print('PostgreSql')
elif opcao_banco == 3:
    dict_candidato['banco'] = 'mysqlserver'
    print('MySqlServer')

print(dict_candidato)
person = Candidato(dict_candidato)
pessoa = CandidatoDao(dict_candidatos_validos, dict_equipes)
print(pessoa.validar_candidato(person))

if 'Valido' == pessoa.validar_candidato(person):
    for i in range(3):
        time.sleep(1)
        print('Verificando equipe adequada....')

    print(pessoa.cadastrar_na_equipe(person))
    opcao_add = input('Em que equipe deseja adicionar o candidato:\n 1- PADAWAN\n 2- LABS\n 3- LOLITA\n: ')

    if opcao_add == '1':
        if 'PADAWAN' != pessoa.cadastrar_na_equipe(person):
            print('Usuário incompativel com equipe PADAWAN!')

        else:
            print(f'Adicionado com sucesso na equipe {cor.amarelo}PADAWAN{cor.fecha_cor}!!')

    elif opcao_add == '2':
        if 'LABS' != pessoa.cadastrar_na_equipe(person):
            print('Usuário incompativel com equipe LABS!')
        else:
            print(f'Adicionado com sucesso na equipe {cor.amarelo}LABS{cor.fecha_cor}!!')


    elif opcao_add == '3':
        if 'LOLITA' != pessoa.cadastrar_na_equipe(person):
            print('Usuário incompativel com equipe LOLITA!')
        else:
            print(f'Adicionado com sucesso na equipe {cor.amarelo}LOLITA{cor.fecha_cor}!!')
    