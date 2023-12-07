from __future__ import annotations
import threading

import processos; from processos import Processo


def read_processes(lista_de_novos_processos: list[Processo]) ->None:

	file = open("processes.txt")
	lines = file.readlines()

	final_lines:list[list[int]] = []
	for line in lines:
		new_line: list[str] = line.split(", ")

		final_line:list[int] = []
		for i, element in enumerate(new_line):
			new_element:str = element.replace("\n","")
			
			final_line.append(int(new_element))

		final_lines.append(final_line)

	lista_de_processos_novos: list[Processo] = []

	for i, value in enumerate(final_lines):
		process_id:int = i
		memory_offset:int = 0

		novo_processo: Processo = \
		Processo(int(value[0]), int(value[1]), int(value[2]), int(value[3]),\
			int(value[4]), int(value[5]), int(value[6]), int(value[7]),\
			int(process_id), int(memory_offset))

		lista_de_novos_processos.append(novo_processo);



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

		nova_operacao["pid"] = int(new_line[0])
		nova_operacao["codigo_operacao"] = int(new_line[1])
		nova_operacao["nome_do_arquivo"] = new_line[2]

		if (nova_operacao["codigo_operacao"] == 0):
			nova_operacao["quantidade_blocos"] = new_line[3]

		list_file_operations.append(nova_operacao)

	return blocos_disco
