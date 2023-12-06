from __future__ import annotations 
import threading; from threading import Thread, Lock
import time; from time import sleep
import copy;
import pdb

import auxiliar
from auxiliar import read_processes, read_files

import processos
from processos import Processo

import gerencia_de_memoria  
from gerencia_de_memoria import Memoria

import filas  
from filas import Fila_Global

import gerenciador_de_arquivos
from gerenciador_de_arquivos import Arquivo

arquivos:Arquivo

lista_de_processos_prontos: list[Processo] = []
fila_global: Fila_Global = Fila_Global(lista_de_processos_prontos)

todos_processos_inicializados: bool = False

tamanho_memoria_principal:int = 30
area_tempo_real:int = 10
area_usuarios:int = 20
memoria: Memoria =\
	 Memoria(tamanho_memoria_principal,area_tempo_real, area_usuarios)

# referente a regiao critica: lista_de_processos_prontos
lock = Lock()
lock_processos_inicializados = Lock()


def main() -> None:

	lista_de_novos_processos: list[Processo] = []

	read_processes(lista_de_novos_processos)

	# usado para debug somente
	"""
	print("conteudo do arquivo processes.txt:")
	for processo in lista_de_novos_processos:
		print(processo)
	"""

	list_file_operations: list[dict[str, str | int] ] = []
	arquivos_na_memoria: list[dict[str, str | int] ] = []

	blocos_disco:int = \
					read_files(list_file_operations, arquivos_na_memoria)

	# usado para debug somente
	"""
	print(f"Numero de blocos: {blocos_disco}")
	print("conteudo do arquivo files.txt:------------------")

	print("lista de arquivos na memoria: ")
	for arquivo in arquivos_na_memoria:
		print(arquivo)

	print("lista de operacoes nos arquivos: ")
	for file_operation in list_file_operations:
		print(file_operation)
	"""

	global arquivos
	arquivos = Arquivo(blocos_disco, arquivos_na_memoria, list_file_operations)

	# começa a contagem e manda cada processo para o escalonador no seu
	# tempo de inicializacao adequado e portanto tambem insere o processo
	# na tabela de processos(cria um PCB) se houver memoria suficiente
	thread_inicializa_processos = \
	 Thread(target=inicializa_processos,\
	 	 args=(lista_de_novos_processos,))

	# inicializa o escalonador de processos
	thread_escalona_processos = Thread(target=escalona_processos)

	thread_inicializa_processos.start()
	thread_escalona_processos.start()

	thread_inicializa_processos.join()
	
	print("Todos os processos foram inicializados!")

	thread_escalona_processos.join()

	print("Todos os processos completados!")
	print("Estado final dos dados no disco: ")
	print(arquivos.dados_no_disco)


def inicializa_processos(lista_de_novos_processos: list[Processo]) ->None:
	instante_atual:int = 0
	pid_processo:int = 0 
	processos_inicializados:int = 0 

	while True:
		time.sleep(1) # waits 1000 miliseconds
		instante_atual+= 1

		print(f"Tempo atual: {instante_atual}")
		
		for processo in lista_de_novos_processos:
			if processo.instante_de_inicializacao == instante_atual:

				lock.acquire()

				conseguiu_alocar:bool = memoria.tenta_alocar(processo)
				if (conseguiu_alocar == False):
					print("Erro sem memoria disponivel!")
				elif (conseguiu_alocar == True):
					processo.pid = pid_processo
					pid_processo+=1

					processo.estado = "pronto"

					# faz deep copy
					lista_de_processos_prontos.append(copy.deepcopy(processo))
					print("Processo carregado na memoria e inserido na lista de processos prontos:")
					print(processo)

				processos_inicializados+=1 

				lock.release()


		#print(f"processos inicializados: {processos_inicializados}")

		#print(f"numero de processos prontos: {len(lista_de_processos_prontos)}")


		if processos_inicializados == len(lista_de_novos_processos):
			lock_processos_inicializados.acquire()

			global todos_processos_inicializados
			todos_processos_inicializados = True

			lock_processos_inicializados.release()

			break


def escalona_processos() -> None:

	while True:
		#regiao critica
		lock.acquire()

		prox_processo: Processo =\
				fila_global.obtem_prox_processo(lista_de_processos_prontos)

		lock.release()

		if (prox_processo.estado != "invalido"):

			#carrega_contexto_anterior()
			#carrega_context_atual()
			executa_processo(prox_processo)


			if (prox_processo.estado == "pronto"):
				
				fila_global.adiciona_processo(copy.deepcopy(prox_processo))
			elif (prox_processo.estado == "finalizado"):
				pass
			elif (prox_processo.estado == "bloqueado"):
				pass 

		lock_processos_inicializados.acquire()

		if (fila_global.esta_vazia() == True and \
			todos_processos_inicializados):
			break
		
		lock_processos_inicializados.release()


def executa_processo(processo: Processo)->None:
	linha:int = processo.linha_atual  # carrega contexto

	for i in range(processo.quantum):
		time.sleep(0.5)
		print(f"Processo: {processo.pid} instruction {linha+1}");
		arquivos.executa_operacao(processo)

		linha+=1
		processo.tempo_restante-= 1
		if (processo.tempo_restante <= 0):
			processo.estado = "finalizado"
			break
		
	processo.linha_atual = linha # salva contexto


if __name__ == "__main__":
	main()

