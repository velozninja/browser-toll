import datetime
import asyncio
from configscs import ConfigcodeSCS
from configscs import ConfiglogSCS
import time
import aply_config as pc



ct = pc.central = ConfigcodeSCS(

    task=pc.task_usuario(),

    regras="não quebrar as diretrizes dos sites ao navegar neles"
)


resultados = asyncio.run(pc.rodar(ct))






tasklog = f"voce OBRIGATORIAMENTE deve criar um arquivo json com o nome log com os seguintes campo timestamp, task q é igual a variavel{pc.task_usuario}, result que é igual a varievel {resultados} só q resumidas a ponto q um humano poça ler de forma humanizada e quando oa rquivo json foi atualizado por voce e quando voce for atualizar o arquivo json voce OBRIGATORIAMENTE vai manter a estrutura de organização que ele se encontra"

ctlog = pc.centrallog = ConfiglogSCS(

    regras="não quebrar as diretrizes dos sites ao navegar neles",

    tasklog=tasklog
)


log_resultados = asyncio.run(pc.rodar_log(ctlog))
time.sleep(5)
print("-------------------------------")
print("Execução sendo verificada.")



time.sleep(5)
print("Execução finalizada.")
print("-------------------------------")

