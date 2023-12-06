
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

		for index, operation in enumerate(self.list_file_operations):
			if operation["pid"] == processo.pid:
				if (operation["codigo_operacao"] == 0):
					conseguiu_criar:bool = self.tenta_criar_arquivo(\
						str(operation["nome_do_arquivo"]),\
						int(operation["quantidade_blocos"])
						)

					if not conseguiu_criar:
						print("Nao ha memoria suficiente ",end='')
						print(f"para criar o arquivo {operation['nome_do_arquivo']}")
					else:
						print(f"Arquivo {operation['nome_do_arquivo']}",end='')
						print(f" criado com sucesso!")

				elif (operation["codigo_operacao"] == 1):
					if (processo.prioridade == 0 or \
						(processo.prioridade != 0 and \
						(processo.nome_arquivo_criado == str(operation["nome_do_arquivo"])
						))
						):
						self.tenta_deletar_arquivo(str(operation["nome_do_arquivo"]))

						print(f"Arquivo {operation['nome_do_arquivo']} ",end='')
						print(f"deletado com sucesso!")
					else:
						print(f"Erro ao deletar o arquivo ",end='')
						print(f" {operation['nome_do_arquivo']}")

				self.list_file_operations.pop(index)

			#print(self.dados_no_disco)
	
	def tenta_criar_arquivo(self, nome_do_arquivo:str, quantidade_blocos:int) ->bool:
		conseguiu_criar: bool = False

		i:int = 0
		while i < len(self.dados_no_disco):
			dado:str = self.dados_no_disco[i]
			if dado == "*":
				j:int = i 
				bloco_inicial:int = i
				total:int = 0
				#print(f"i = {i}")
				while j < len(self.dados_no_disco) and\
						self.dados_no_disco[j] == "*" and \
						self.mapa_de_bits[j] == 0:

						j+= 1
						total+= 1


				#print(f"total : {total}")
				if total >= quantidade_blocos:
					for k in range(bloco_inicial, bloco_inicial+quantidade_blocos):

						self.dados_no_disco[k] = nome_do_arquivo
						self.mapa_de_bits[k] = 1

					conseguiu_criar = True
					break

				
			i+= 1

		return conseguiu_criar

	def tenta_deletar_arquivo(self, nome_do_arquivo: str) -> bool:
		conseguiu_deletar: bool = False 

		for i, dado in enumerate(self.dados_no_disco):
			if dado == nome_do_arquivo:
				j:int = i 
				while j < len(self.dados_no_disco) and \
						self.dados_no_disco[j] == nome_do_arquivo and\
						self.mapa_de_bits[j] == 1:

						self.dados_no_disco[j] = "*"
						self.mapa_de_bits[j] = 0
						j+= 1

				break


		conseguiu_deleta = True
		return conseguiu_deletar

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

