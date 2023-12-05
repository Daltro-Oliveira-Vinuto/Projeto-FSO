from __future__ import annotations 
import threading; from threading import Thread, Lock
import time; from time import sleep


import auxiliar
from auxiliar import read_processes, read_files

import processos
from processos import Processo

import memoria  
from memoria import Memoria

lista_de_processos_prontos: list[Processo] = []

# referente a regiao critica: lista_de_processos_prontos
lock = Lock() 


def main() -> None:
	memoria: Memoria = Memoria(1024)

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


	# começa a contagem e manda cada processo para o escalonador no seu
	# tempo de inicializacao adequado e portanto tambem insere o processo
	# na tabela de processos(cria um PCB) se houver memoria suficiente
	thread_inicializa_processos = \
	 Thread(target=inicializa_processos,\
	 	 args=(lista_de_novos_processos, memoria,))

	# inicializa o escalonador de processos
	thread_escalona_processos = Thread(target=escalona_processos)

	thread_inicializa_processos.start()
	thread_escalona_processos.start()

	thread_inicializa_processos.join()
	
	print("Todos os processos foram inicializados!")

	thread_escalona_processos.join()




def inicializa_processos(lista_de_novos_processos: list[Processo], \
						 memoria: Memoria) ->None:
	instante_atual:int = 0
	pid_processo:int = 0  

	processos_inicializados:int = 0

	while True:
		time.sleep(1) # waits 1000 miliseconds
		instante_atual+= 1

		print(f"numero de processos prontos: {len(lista_de_processos_prontos)}")
		print(f"Tempo atual: {instante_atual}")
		
		for processo in lista_de_novos_processos:
			if processo.instante_de_inicializacao == instante_atual:
				lock.acquire()

				memory_offset: int = memoria.tenta_alocar(processo.blocos)
				if (memory_offset == -1):
					print("Erro sem memoria disponivel!")
				else:
					processo.pid = pid_processo
					processo.memory_offset = memory_offset
					pid_processo+=1
					lista_de_processos_prontos.append(processo)

				lock.release()

				processos_inicializados+=1 

		if processos_inicializados == len(lista_de_novos_processos):
			break








def escalona_processos() -> None:

	while True:
		#regiao critica
		lock.acquire()



		lock.release()
		

if __name__ == "__main__":
	main()