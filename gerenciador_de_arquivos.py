
import processos; from processos import Processo

class Arquivo:
	def __init__(self, blocos_disco:int, \
				arquivos_na_memoria: list[dict[str, str | int] ], \
				list_file_operations: list[dict[str, str | int] ]):
		self.blocos_disco:int = blocos_disco
		self.arquivos_na_memoria: list[dict[str, str | int] ] = arquivos_na_memoria
		self.list_file_operations: list[dict[str, str | int] ] = list_file_operations

		self.inicializa_sistema_arquivos()

		
	def executa_operacao(self, processo: Processo) ->None:
		#print(f"numero de blocos: {self.blocos_disco}")
		#print(f"dados no disco: {self.dados_no_disco}")
		pass

	def inicializa_sistema_arquivos(self) -> None:
		self.mapa_de_bits: list[int] = [0 for x in range(self.blocos_disco)]
		self.dados_no_disco: list[str] = ["*" for x in range(self.blocos_disco)]

		for dado in self.arquivos_na_memoria:
			posicao_inicial:int = int(dado["bloco_inicial"])
			posicao:int = posicao_inicial

			for i in range(int(dado["blocos_ocupados"])):
				self.dados_no_disco[posicao] = str(dado["nome_do_arquivo"])
				self.mapa_de_bits[posicao] = 1
				posicao+= 1

