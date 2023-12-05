from __future__ import annotations 

import auxiliar
from auxiliar import read_processes

import processos
from processos import Processo

import memoria  
from memoria import Memoria

def main() -> None:
	memoria: Memoria = Memoria(1024)

	lista_de_processos: list[Processo];

	lista_de_processos = read_processes(memoria)

	for p in lista_de_processos:
		print(p)

if __name__ == "__main__":
	main()