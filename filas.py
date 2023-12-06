import processos; from processos import Processo

class Fila_Global:

    def __init__(self, fila_processos_prontos: list[Processo]):
        self.fila_tempo_real: list[Processo] = []
        self.filas_usuario: list[list[Processo]] = [[] for _ in range(3)]
        self.ordena_processos_prontos(fila_processos_prontos)

    def obtem_prox_processo(self, fila_processos_prontos: list[Processo]) -> Processo:
        self.ordena_processos_prontos(fila_processos_prontos)
        if self.fila_tempo_real:
            return self.fila_tempo_real.pop(0)
        elif any(self.filas_usuario):
            # Encontrar a primeira fila de usuário não vazia
            for fila_usuario in self.filas_usuario:
                if fila_usuario:
                    return fila_usuario.pop(0)
        return Processo(-1, -1, -1, -1, False, False, False, False, -1, -1)

    def ordena_processos_prontos(self, fila_processos_prontos: list[Processo]) -> None:
        for processo in fila_processos_prontos:
            if processo.prioridade == 0:
                self.fila_tempo_real.append(processo)
            elif 1 <= processo.prioridade <= 3:
                self.filas_usuario[processo.prioridade - 1].append(processo)

        # Ordena as filas de usuário por prioridade
        for prioridade in range(3):
            self.filas_usuario[prioridade] = sorted(self.filas_usuario[prioridade], key=lambda x: x.prioridade)

    def esta_vazia(self) -> bool:
        return not (self.fila_tempo_real or any(self.filas_usuario))

    def adiciona_processo(self, novo_processo: Processo) -> None:
        # Adiciona o processo à fila correspondente
        if novo_processo.prioridade == 0:
            self.fila_tempo_real.append(novo_processo)
        elif 1 <= novo_processo.prioridade <= 3:
            self.filas_usuario[novo_processo.prioridade - 1].append(novo_processo)
        # Reordena as filas após a adição
        self.ordena_processos_prontos([])