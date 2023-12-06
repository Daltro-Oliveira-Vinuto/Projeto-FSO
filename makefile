
all: clear mypy interpret
load: interpret

clear:
	clear

mypy:
	mypy kernel.py auxiliar.py processos.py filas.py gerenciador_de_io.py gerencia_de_memoria.py gerenciador_de_arquivos.py

interpret:
	python3 kernel.py

debug:
	pdb kernel.py