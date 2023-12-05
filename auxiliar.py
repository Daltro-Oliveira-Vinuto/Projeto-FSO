from __future__ import annotations

import processos
from processos import Processo
import memoria
from memoria import Memoria

def read_processes(memoria: Memoria) ->list[Processo]:

	file = open("processes.txt")
	lines = file.readlines()

	final_lines:list[list[int]] = []
	for line in lines:
		new_line:str = line.split(", ")

		final_line:list[int] = []
		for i, element in enumerate(new_line):
			new_element:str = element.replace("\n","")
			
			final_line.append(int(new_element))

		final_lines.append(final_line)

		

	lista_de_processos: list[Processo] = []

	for i, line in enumerate(final_lines):

		memory_offset:int = memoria.tenta_alocar(line[3])

		novo_processo: Processo = \
		Processo(line[0],line[1],line[2],line[3],\
			line[4], line[5], line[6],line[7],\
			i,memory_offset)

		lista_de_processos.append(novo_processo);


	return lista_de_processos


def read_files(list_file_operations: list[ dict[str, str | int] ],\
				arquivos_na_memoria: list[ dict[str, str | int] ]) -> int:

	file = open("files.txt")

	lines = file.readlines()

	blocos_disco:int = int(lines[0])

	segmentos_ocupados:int = int(lines[1])

	for i in range(2, segmentos_ocupados+2):
		line:str = lines[i]

		new_line:list[str] = line.split(", ")
		new_line[2] = new_line[2].replace("\n","")

		arquivo_na_memoria: dict[str, str | int ] = dict()

		arquivo_na_memoria["nome_do_arquivo"] = new_line[0]
		arquivo_na_memoria["bloco_inicial"] = int(new_line[1])
		arquivo_na_memoria["blocos_ocupados"] = int(new_line[2])

		arquivos_na_memoria.append(arquivo_na_memoria)


	linha_inicial_operacoes:int = segmentos_ocupados+2

	for i in range(linha_inicial_operacoes, len(lines)):
		line = lines[i]

		new_line = line.split(", ")
		new_line[-1] = new_line[-1].replace("\n","")

		nova_operacao: dict[str, str | int] = dict()

		nova_operacao["id"] = int(new_line[0])
		nova_operacao["codigo_operacao"] = int(new_line[1])
		nova_operacao["nome_arquivo"] = new_line[2]

		if (nova_operacao["codigo_operacao"] == 0):
			nova_operacao["quantidade_blocos"] = new_line[3]

		list_file_operations.append(nova_operacao)







	return blocos_disco