import processos; from processos import Processo


class Fila_Global:

    def __init__(self, fila_processos_prontos: list[Processo]):
        #self.fila_global: list[Processo] = []
        self.ordena_processos_prontos(fila_processos_prontos)

        self.fila_tempo_real: list[Processo] = []
        self.filas_usuarios: list[list[Processo]] = [[] for _ in range(3)]
        self.maxima_quantidade:int = 1000

    def obtem_prox_processo(self, fila_processos_prontos: list[Processo])\
        -> Processo:

        self.ordena_processos_prontos(fila_processos_prontos)

        """
        if not self.esta_vazia():
            return self.fila_global.pop(0)
        else:
            processo_invalido: Processo = \
                Processo(-1,-1,-1,-1,False,False,False,False,-1,-1)
            processo_invalido.estado = "invalido"
            return processo_invalido
        """

        if len(self.fila_tempo_real) > 0:
            return self.fila_tempo_real.pop(0)

        elif len(self.filas_usuarios[0]) > 0:
            return self.filas_usuarios[0].pop(0)
        elif len(self.filas_usuarios[1]) > 0:
            return self.filas_usuarios[1].pop(0)
        elif len(self.filas_usuarios[2]) > 0:
            return self.filas_usuarios[2].pop(0)
        else:
            processo_invalido: Processo = \
                Processo(-1,-1,-1,-1,False,False,False,False,-1,-1)
            processo_invalido.estado = "invalido"
            return processo_invalido

    def ordena_processos_prontos(self, \
        fila_processos_prontos: list[Processo]) ->None:

        """
        nova_fila: list[Processo] = []
        numero_processos_prontos:int = len(fila_processos_prontos)
        for i in range(numero_processos_prontos):
            novo_processo: Processo = fila_processos_prontos.pop()
            nova_fila.append(novo_processo)

        self.fila_global+= nova_fila
        """

        nova_fila: list[Processo] = []
        numero_processos_prontos:int = len(fila_processos_prontos)
        for i in range(numero_processos_prontos):
            novo_processo: Processo = fila_processos_prontos.pop()
            nova_fila.append(novo_processo)

        for novo_processo in nova_fila:
            if novo_processo.prioridade == 0 and \
                self.get_numero_processos() < self.maxima_quantidade:
                self.fila_tempo_real.append(novo_processo)
            else:
                if novo_processo.prioridade == 1 and \
                    self.get_numero_processos() < self.maxima_quantidade:
                    self.filas_usuarios[0].append(novo_processo)
                elif novo_processo.prioridade == 2 and \
                    self.get_numero_processos() < self.maxima_quantidade:
                    self.filas_usuarios[1].append(novo_processo)
                elif novo_processo.prioridade >= 3 and \
                    self.get_numero_processos() < self.maxima_quantidade:
                    self.filas_usuarios[2].append(novo_processo)

    def get_numero_processos(self) -> int:
        total_processos:int = 0 

        total_processos+= len(self.fila_tempo_real)

        for fila_usuario in self.filas_usuarios:
            total_processos+= len(fila_usuario)

        return total_processos



    def esta_vazia(self) ->bool:
        if (self.get_numero_processos() == 0):
            return True
        else:
            return False

    def adiciona_processo(self, novo_processo: Processo) ->None:
        
        if novo_processo.prioridade == 0 and \
            self.get_numero_processos() < self.maxima_quantidade:
            self.fila_tempo_real.append(novo_processo)
        else:
            if novo_processo.prioridade == 1 and \
                self.get_numero_processos() < self.maxima_quantidade:
                self.filas_usuarios[0].append(novo_processo)
            elif novo_processo.prioridade == 2 and \
                self.get_numero_processos() < self.maxima_quantidade:
                self.filas_usuarios[1].append(novo_processo)
            elif novo_processo.prioridade >= 3 and \
                self.get_numero_processos() < self.maxima_quantidade:
                self.filas_usuarios[2].append(novo_processo)






