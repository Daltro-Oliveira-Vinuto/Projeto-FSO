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