import processos; from processos import Processo


class Fila_Global:

	def __init__(self, fila_processos_prontos: list[Processo]):
		self.fila_global = \
			self.ordena_processos_prontos(fila_processos_prontos)

	def obtem_prox_processo(self, fila_processos_prontos: list[Processo])\
		-> Processo:

		self.fila_global = self.ordena_processos_prontos(fila_processos_prontos)

		if not self.esta_vazia():
			return self.fila_global.pop(0)
		else:
			processo_invalido: Processo = \
				Processo(-1,-1,-1,-1,False,False,False,False,-1,-1)
			processo_invalido.estado = "invalido"
			return processo_invalido

	def ordena_processos_prontos(self, \
		fila_processos_prontos: list[Processo])->list[Processo]:

		nova_fila: list[Processo] = []
		numero_processos_prontos:int = len(fila_processos_prontos)
		for i in range(numero_processos_prontos):
			novo_processo: Processo = fila_processos_prontos.pop()
			nova_fila.append(novo_processo)

		return nova_fila


	def esta_vazia(self) ->bool:
		if (len(self.fila_global) == 0):
			return True
		else:
			return False

	def adiciona_processo(self, novo_processo: Processo) ->None:
		self.fila_global.append(novo_processo)






