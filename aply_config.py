"""Helpers de configuração e execução de agentes.

Este módulo expõe funções utilitárias usadas pelo script principal
(`main.py`) para ler input do usuário e orquestrar a execução dos
agentes definidos em `configscs.py`.

Documentação e comentários estão em Português (BR).
"""

import dotenv
from configscs import ConfigcodeSCS
from configscs import ConfiglogSCS

import configscs as cf
import asyncio
import datetime


def task_usuario():
    """Lê a tarefa do usuário via input.

    Retorna a string digitada pelo usuário. Exemplo de uso:
        tarefa = task_usuario()
    """
    return input("Digite sua tarefaa: ")










# Instâncias padrão usadas pelo fluxo principal. Valores iniciais são
# vazios e normalmente sobrescritos quando o script principal solicita
# a entrada do usuário.
central = ConfigcodeSCS(
    task="",
    regras="não quebrar as diretrizes dos sites ao navegar neles"
)
centrallog = ConfiglogSCS(

    tasklog="" ,
    regras="não quebrar as diretrizes dos sites ao navegar neles"
)


async def rodar(central):
    """Wrapper assíncrono que protege a execução do agente com checagem offline.

    Args:
        central (ConfigcodeSCS): instância configurada do agente de código.

    Lança `RuntimeError` se `configscs.online` for `False`, caso contrário
    executa `central.run_code()` e retorna seus resultados.
    """
    if cf.online is False:
        raise RuntimeError("Sistema offline. Operação cancelada.")

    else:
        resultados = await central.run_code()
        return resultados



async def rodar_log(centrallog):
    """Wrapper assíncrono para executar o agente de log com checagem offline.

    Args:
        centrallog (ConfiglogSCS): instância configurada do agente de log.

    Retorna o resultado de `centrallog.run_log(...)` ou lança `RuntimeError`
    se o sistema estiver offline.
    """
    if cf.online is False:
        raise RuntimeError("Sistema offline. Operação cancelada.")
    
    else:
        log_resultados = await centrallog.run_log(log_task=centrallog.tasklog)
        return log_resultados
    


