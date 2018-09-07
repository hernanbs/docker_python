#!/usr/bin/python3
# -*- coding: utf-8 -*-
import psycopg2

class ConnectionFactory(object):
    '''Fabrica de conexão com o banco de dados.'''
	ISOLATION_SERIALIZABLE = psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE
    def __init__(self):
        self.__conn = None
        self.STRINGCONNECTION = 'dbname=postgres user=postgres  host=192.168.61.200 port=54300'

    def get_connection(self,isolation=ISOLATION_SERIALIZABLE,read_only=False):
        ''' Garante uma única conexão ao banco de dados com sessao configurada'''
        if self.__conn is None:
            try:
                self.__conn = psycopg2.connect(self.STRINGCONNECTION)
		self.__conn.set_session(isolation_level=isolation,readonly=read_only, autocommit=False)
            except (psycopg2.Error, AttributeError) as e:
                print(e)
                self.__conn = None
        return self.__conn

# Teste conexão  psql --dbname=postgres -U postgres  -h 192.168.61.200 -p 54300
#
# class Conexao(object):
#     @staticmethod
#     def atualizar(conexao, identificador, txt_set):
#         '''Atualiza dados da tabela'''
# 	# TODO alterar para uma unica tabela e mudar nome de classe para um Objeto DAO
#         try:
#             cursor = conexao.cursor()
#             q = ' UPDATE tb_tabela '
#             q = q + ' SET  ' + txt_query
#             q = q + ' WHERE id = ' + str(identificador)
#             # print(q)
#             cursor.execute(q)
#             cursor.close()
#         except  (psycopg2.Error, AttributeError) as e:
#             print(e)

    # @staticmethod
    # def inserir(conexao):
	# # TODO mudar parametros para usar um objeto 
    #     '''Insere um novo pedido para corte na tabela com informações basicas'''
    #     try:
    #         cursor = conexao.cursor()
    #         q = 'INSERT INTO tb_tabela'
    #         q = q + ' (id) '
    #         q = q + ' VALUES ()'
    #         cursor.execute(q)
    #         cursor.close()
    #     except (psycopg2.Error, AttributeError) as e:
    #         print(e)

    # @staticmethod
    # def listar(conexao, select,):
    #     '''Lista todos objetos'''
    #     # TODO verificar nome de campos na tabela usada 
    #     try:
    #         cursor = conexao.cursor()
    #         q = "SELECT " + select
    #         q = q + " FROM tb_tabela"
    #         #q = q + " WHERE"
    #         cursor.execute(q)
    #         linha = cursor.fetchall()
    #     except UnboundLocalError:
    #         linha = []
    #     except Exception as e:
    #         print(e)

    #     return linha

if __name__ == "__main__":
    print('Testando')

	
