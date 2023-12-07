
from __future__ import annotations 

import processos; from processos import Processo 


class IO_Hierarquia:

	def __init__(self) -> None:
		self.recursos:list[int] = [2, 1, 1, 2]

	def tenta_alocar(self, processo: Processo) ->bool:
		conseguiu_alocar: bool = False 

		if (processo.impressora > 0 and (self.recursos[0] - processo.impressora) >= 0):
			self.recursos[0]-= processo.impressora

			conseguiu_alocar = True


		if processo.scanner > 0 and (self.recursos[1] - processo.scanner >= 0):
			self.recursos[1]-= processo.scanner  

			conseguiu_alocar = True

		if processo.modem > 0 and (self.recursos[2] - processo.modem >= 0):
			self.recursos[2]-= processo.modem

			conseguiu_alocar = True

		if processo.disco > 0 and (self.recursos[3] - processo.disco >= 0):
			self.recursos[3]-= processo.disco

			conseguiu_alocar = True

		if (processo.impressora == 0 and\
			processo.scanner == 0 and\
			processo.modem == 0 and \
			processo.disco == 0):

			conseguiu_alocar = True

		return conseguiu_alocar

	def desaloca_recurso(self, processo: Processo) ->None:

		self.recursos[0]+= processo.impressora
		self.recursos[1]+= processo.scanner
		self.recursos[2]+= processo.modem
		self.recursos[3]+= processo.disco

