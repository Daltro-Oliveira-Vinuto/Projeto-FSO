
all: clear mypy interpret 

clear:
	clear

mypy:
	mypy OS.py auxiliar.py processos.py filas.py io.py memoria.py arquivos.py

interpret:
	python3 OS.py