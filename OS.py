from __future__ import annotations 

import auxiliar
from auxiliar import read_processes, read_files

import processos
from processos import Processo

import memoria  
from memoria import Memoria

def main() -> None:
	memoria: Memoria = Memoria(1024)

	lista_de_processos: list[Processo];

	lista_de_processos = read_processes(memoria)

	print("conteudo do arquivo processes.txt:")
	for p in lista_de_processos:
		print(p)


	list_file_operations: list[dict[str, str | int] ] = []
	arquivos_na_memoria: list[dict[str, str | int] ] = []

	blocos_disco:int = \
					read_files(list_file_operations, arquivos_na_memoria)

	print(f"Numero de blocos: {blocos_disco}")
	print("conteudo do arquivo files.txt:------------------")

	print("lista de arquivos na memoria: ")
	for arquivo in arquivos_na_memoria:
		print(arquivo)

	print("lista de operacoes nos arquivos: ")
	for file_operation in list_file_operations:
		print(file_operation)





if __name__ == "__main__":
	main()