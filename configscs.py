"""Configuração dos agentes usados pelo projeto.

Este módulo fornece classes que encapsulam a criação e execução de
`CodeAgent` (via `ChatBrowserUse`) para duas finalidades principais:
- `ConfigcodeSCS`: executar uma tarefa de código/automação
- `ConfiglogSCS`: executar uma tarefa de geração/atualização de logs

Todas as mensagens e documentação estão em Português (BR).
"""

from browser_use import CodeAgent, ChatBrowserUse, Browser
from dotenv import load_dotenv
import os
import asyncio


# Flag simples para habilitar/desabilitar execução online
online = True

# Carrega variáveis de ambiente do arquivo .env (se existir)
load_dotenv()

# Verificação mínima: a chave usada pelo serviço externo deve existir
if "BROWSER_USE_API_KEY" not in os.environ:
    raise RuntimeError("BROWSER_USE_API_KEY não existe no ambiente")

#definindo configuração do agente de codigo feito usandoa  biblioteca Browser Use
class ConfigcodeSCS:
    def __init__(self, task: str,  regras: str):
        self.task = task


        self.regras = regras

        self.agentcode = CodeAgent(
            llm=ChatBrowserUse(),
            task=self.task,
            rules=self.regras,
        )
        #comando para rodar
    async def run_code(self):




        print("▶ Iniciando CodeAgent...")
        code_result = await self.agentcode.run()
        print("▶ CodeAgent finalizado.")


        return {
            "code_agent": code_result,
          
        }

#criando o agente de log com a biblioteca Browser Use
class ConfiglogSCS:
    browser = Browser(headless=True)
    def __init__(self,   regras: str, tasklog: str, browser):
        self.browser = browser

        self.tasklog = tasklog

        self.regras = regras

        self.agent_log = CodeAgent(
            llm=ChatBrowserUse(),
            task=self.tasklog,
            rules=self.regras,
            browser=self.browser
        )
        #comando para rodar
    async def run_log(self, log_task: str):
        print("▶ Iniciando Agent Log...")
        log_result = await self.agent_log.run()
        print("▶ Agent Log finalizado.")
        return {
            "agent_log": log_result,
        }
    

