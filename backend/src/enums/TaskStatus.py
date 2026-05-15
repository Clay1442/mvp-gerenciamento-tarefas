from enum import Enum

class TaskStatus(str, Enum):
    PENDENTE = "Pendente"
    EM_PROGRESSO = "Em_progresso"
    COMPLETO = "Completo"