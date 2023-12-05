
all: clear mypy interpret 

clear:
	clear

mypy:
	mypy kernel.py auxiliar.py processos.py filas.py io.py memoria.py arquivos.py

interpret:
	python3 kernel.py