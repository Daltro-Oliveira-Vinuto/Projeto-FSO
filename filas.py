import processos; from processos import Processo
from typing import Dict

class Fila_Global:

    def __init__(self, fila_processos_prontos: list[Processo]):
        self.fila_global = self.ordena_processos_prontos(fila_processos_prontos)

    def obtem_prox_processo(self, fila_processos_prontos: list[Processo]) -> Processo:
        # fila ordenada
        self.fila_global = self.ordena_processos_prontos(fila_processos_prontos)

        if not self.esta_vazia():
            return self.fila_global.pop(0)
        else:
            processo_invalido: Processo = Processo(-1, -1, -1, -1, False, False, False, False, -1, -1)
            processo_invalido.estado = "invalido"
            return processo_invalido

    def ordena_processos_prontos(self, fila_processos_prontos: list[Processo]) -> list[Processo]:
        fila_tempo_real: list[Processo] = []
        filas_usuario: Dict[int, list[Processo]] = {0: [], 1: [], 2: []}

        for processo in fila_processos_prontos:
            if processo.prioridade == 0:
                fila_tempo_real.append(processo)
            elif 1 <= processo.prioridade <= 3:
                filas_usuario[processo.prioridade].append(processo)

        # Ordena as filas de usuário por prioridade
        for prioridade in range(1, 4):
            filas_usuario[prioridade] = sorted(filas_usuario[prioridade], key=lambda x: x.prioridade)

        # Concatena as filas de tempo real e de usuário para formar a fila global
        nova_fila = fila_tempo_real + filas_usuario[0] + filas_usuario[1] + filas_usuario[2]

        return nova_fila

    def esta_vazia(self) -> bool:
        return len(self.fila_global) == 0

    def adiciona_processo(self, novo_processo: Processo) -> None:
        self.fila_global.append(novo_processo)