from __future__ import annotations
import processos; from processos import Processo;
import pdb

class Memoria:
	def __init__(self, total_de_memoria:int):
		self.total_de_memoria:int = total_de_memoria

		# 0 significa vazio e 1 ocupado
		self.mapa_de_bits = [0 for x in range(total_de_memoria)]

	def tenta_alocar(self, processo: Processo) ->bool:
		#pdb.set_trace()

		conseguiu_alocar: bool = False
		
		i:int = 0 
		while not conseguiu_alocar and i < len(self.mapa_de_bits):

			if self.mapa_de_bits[i] == 1: 
				i+=1
			elif self.mapa_de_bits[i] == 0:
				
				memory_offset = i;

				posicao_vazia:bool = True
				blocos = 0
				while posicao_vazia == True and blocos < processo.blocos \
											and i < self.total_de_memoria:

					if self.mapa_de_bits[i] == 1:
						posicao_vazia = False
						i+=1
						break
					elif self.mapa_de_bits[i] == 0:
						i+=1
						blocos+= 1  

				if posicao_vazia == True and blocos == processo.blocos:
					# aloca espaco no mapa de bits
					for i in range(memory_offset, memory_offset+blocos):
						self.mapa_de_bits[i] = 1 

					processo.memory_offset = memory_offset
					conseguiu_alocar = True
					break
			

		print(self.mapa_de_bits)
		return conseguiu_alocar


	def desaloca(self, processo: Processo) ->None:
		
		for i in range(processo.memory_offset, \
			processo.memory_offset+processo.blocos):
			self.mapa_de_bits[i] = 0