import dotenv
from configscs import ConfigcodeSCS
from configscs import ConfiglogSCS

import configscs as cf
import asyncio
import datetime








def task_usuario():
    return input("Digite sua tarefa: ")










central = ConfigcodeSCS(
    task="",
    regras="não quebrar as diretrizes dos sites ao navegar neles"
)
centrallog = ConfiglogSCS(

    tasklog="" ,
    regras="não quebrar as diretrizes dos sites ao navegar neles"
)


async def rodar(central):
    if cf.online is False:
        raise RuntimeError("Sistema offline. Operação cancelada.")

    else:
        resultados = await central.run_code()
        return resultados



async def rodar_log(centrallog):
    if cf.online is False:
        raise RuntimeError("Sistema offline. Operação cancelada.")
    
    else:
        log_resultados = await centrallog.run_log(log_task=centrallog.tasklog)
        return log_resultados
    


