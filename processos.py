

class Processo:

	def __init__(self,\
		 instante_de_inicializacao:int, prioridade:int, \
		 tempo_de_processador:int, blocos:int, \
		 impressora:bool, scanner:bool, modem:bool, disco:bool,\

		 pid:int, memory_offset:int ):

		self.instante_de_inicializacao:int = instante_de_inicializacao
		self.prioridade:int = prioridade
		self.tempo_de_processador:int = tempo_de_processador
		self.blocos:int = blocos

		self.impressora:bool = impressora
		self.scanner:bool = scanner
		self.modem:bool = modem
		self.disco:bool = disco

		self.pid:int = pid
		self.memory_offset:int = memory_offset

		self.estado:str = "novo"


	def __str__(self) -> str:
		processo_str: str = ""
		processo_str+= f"pid: {self.pid} \n"

		processo_str+= f"instante_de_inicializacao: {self.instante_de_inicializacao} \n"
		processo_str+= f"prioridade: {self.prioridade} \n"
		processo_str+= f"tempo_de_processador: {self.tempo_de_processador} \n"
		processo_str+= f"blocos: {self.blocos} \n"

		processo_str+= f"impressora: {self.impressora} \n"
		processo_str+= f"scanner: {self.scanner} \n"
		processo_str+= f"modem: {self.modem} \n"
		processo_str+= f"disco: {self.disco} \n"

		processo_str+= f"memory_offset: {self.memory_offset} \n"
		processo_str+= f"estado: {self.estado} \n"
		processo_str+= "\n"

		return processo_str
