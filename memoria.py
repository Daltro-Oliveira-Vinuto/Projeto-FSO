from __future__ import annotations


class Memoria:
	def __init__(self, total_de_memoria:int):
		self.total_de_memoria:int = total_de_memoria

	def tenta_alocar(self, quantidade_de_blocos:int) ->int:
		memory_offset: int = 0 

		return memory_offset