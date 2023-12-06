
from __future__ import annotations 

import processos; from processos import Processo 


class IO_Hierarquia:

	def __init__(self) -> None:
		self.recursos:list[list[bool]] = [[False,False], [False], [False], [False,False]]

	def tenta_alocar(self, processo: Processo) ->bool:
		conseguiu_alocar: bool = False 

		if (processo.impressora == True and (self.recursos[0][0] == False or\
											self.recursos[0][1] == False)) or\
		   (processo.scanner == True and self.recursos[1][0] == False) or \
		   (processo.modem == True and self.recursos[2][0] == False) or \
		   (processo.disco == True and (self.recursos[3][0] == False or\
		   								self.recursos[3][1] == False)):

		   conseguiu_alocar = True

		if (processo.impressora == True and self.recursos[0][0] == False):
			self.recursos[0][0] = True  

			return conseguiu_alocar

		elif (processo.impressora == True and self.recursos[0][1] == False):
			self.recursos[0][1] = True  

			return conseguiu_alocar

		elif (processo.scanner == True and self.recursos[1][0] == False):
			self.recursos[1][0] = True  

			return conseguiu_alocar

		elif (processo.modem == True and self.recursos[2][0] == False):
			self.recursos[2][0] = True  

			return conseguiu_alocar

		elif (processo.disco == True and self.recursos[3][0] == False):
			self.recursos[3][0] = True  

			return conseguiu_alocar
		elif (processo.disco == True and self.recursos[3][1] == False):
			self.recursos[3][1] = True

		return conseguiu_alocar

	def desaloca_recurso(self, processo: Processo) ->None:
		if (processo.impressora == True and self.recursos[0][0] == True):
			self.recursos[0][0] = False 
		elif (processo.impressora == True and self.recursos[0][1] == True):
			self.recursos[0][1] = False   

		elif (processo.scanner == True and self.recursos[1][0] == True):
			self.recursos[1][0] = False  

		elif (processo.modem == True and self.recursos[2] == True):
			self.recursos[2][0] = False  

		elif (processo.disco == True and self.recursos[3][0] == True):
			self.recursos[3][0] = False
		elif (processo.impressora == True and self.recursos[3][1] == True):
			self.recursos[3][1] = False  

