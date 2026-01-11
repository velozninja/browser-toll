"""Script principal.

Fluxo:
1. Solicita ao usuário a descrição da tarefa via `task_usuario()` (em `aply_config`).
2. Cria um `ConfigcodeSCS` para executar a tarefa principal e aguarda o resultado.
3. Monta um `tasklog` descritivo e executa o agente de log.

Observação: este arquivo orquestra chamadas assíncronas via `asyncio.run`.
"""


import asyncio
from configscs import ConfigcodeSCS
from configscs import ConfiglogSCS
import time
import aply_config as pc




# Cria/atualiza a instância `central` usando a entrada do usuário.
# A atribuição `pc.central = ...` mantém a instância também disponível
# no módulo `aply_config` para reuso.
ct = pc.central = ConfigcodeSCS(
    task=pc.task_usuario(),
    regras="não quebrar as diretrizes dos sites ao navegar neles"
)



# Executa a tarefa principal do agente e guarda o resultado.
resultados = asyncio.run(pc.rodar(ct))

ctg = pc.central = ConfigcodeSCS(
    task=f"fazer um grafico usando OBRIGATORIAMENTE matplotlib que mais se enquadra com o resultado{resultados} de forma resumida para pessoas também usando em consideranção a variavél {pc.task_usuario}",
    regras="n quebrar regras de sites"
)

grafico = asyncio.run(pc.rodar(ctg))






# Monta um texto de instrução para o agente de log. Esse texto descreve o
# formato esperado do arquivo JSON de log (campos: timestamp, task, result,
# e metadados de atualização). Atenção: aqui o f-string inclui `pc.task_usuario`
# (função) e `resultados` (o retorno do agente) — manter esse comportamento
# preserva a intenção original do código.
tasklog = f"voce OBRIGATORIAMENTE deve criar um arquivo json com o nome log com os seguintes campo timestamp, task q é igual a variavel{pc.task_usuario}, result que é igual a varievel {resultados} só q resumidas a ponto q um humano poça ler de forma humanizada e quando oa rquivo json foi atualizado por voce e quando voce for atualizar o arquivo json voce OBRIGATORIAMENTE vai manter a estrutura de organização que ele se encontra e depois voce irá criar um arquivo de historico de logs e vc vai por informações mais expecificas e na hora de atualizar o historico vc vai adicionar outros campos abaixo dos anterires"

# Cria a instância do agente de log com o texto de tarefa acima.
ctlog = pc.centrallog = ConfiglogSCS(
    regras="não quebrar as diretrizes dos sites ao navegar neles",
    tasklog=tasklog,
    browser=pc.centrallog.browser
)

#execultando agente log
log_resultados = asyncio.run(pc.rodar_log(ctlog))

time.sleep(5)
print("Execução finalizada.")
print("-------------------------------")

