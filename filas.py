class FilaProcessos:
    def __init__(self): #inicializa uma lista vazia chamada processos.
        self.processos = []

    def adicionar_processo(self, processo): #Adiciona um processo à lista de processos.
        self.processos.append(processo)

    def remover_processo(self): #Remove e retorna o primeiro processo na lista (FIFO)
        if not self.vazia():
            return self.processos.pop(0)
        else:
            return None

    def vazia(self): #Retorna True se a lista de processos estiver vazia, False caso contrário.
        return len(self.processos) == 0

#Esta é uma subclasse de FilaProcessos que herda todos os métodos de FilaProcessos.
class FilaTempoReal(FilaProcessos):
    pass


#Esta é outra subclasse de FilaProcessos. Ela adiciona um atributo prioridade durante a inicialização. Cada instância desta classe representa uma fila de processos de usuário com uma prioridade específica.
class FilaUsuario(FilaProcessos): 
    def __init__(self, prioridade):
        super().__init__()
        self.prioridade = prioridade

class ProcessosProntos:
    def __init__(self): #O construtor da classe. Inicializa a fila de tempo real 
        self.fila_tempo_real = FilaTempoReal()
        self.filas_usuario = [FilaUsuario(i) for i in range(1, 4)] #lista de instâncias de FilaUsuario com prioridades de 1 a 3.

    #Adiciona um processo à fila apropriada com base na prioridade do processo. Se a prioridade for 0, adiciona à fila de tempo real. Se a prioridade estiver entre 1 e 3, adiciona à fila de usuário correspondente.
    def adicionar_processo(self, processo):
        if processo.prioridade == 0:
            self.fila_tempo_real.adicionar_processo(processo)
        elif 1 <= processo.prioridade <= 3:
            self.filas_usuario[processo.prioridade - 1].adicionar_processo(processo)