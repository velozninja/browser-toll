from browser_use import CodeAgent, ChatBrowserUse, Agent
from dotenv import load_dotenv
import os
import asyncio


online = True
load_dotenv()

if "BROWSER_USE_API_KEY" not in os.environ:
    raise RuntimeError("BROWSER_USE_API_KEY não existe no ambiente")


class ConfigcodeSCS:
    def __init__(self, task: str,  regras: str):
        self.task = task


        self.regras = regras

        self.agentcode = CodeAgent(
            llm=ChatBrowserUse(),
            task=self.task,
            rules=self.regras,
        )





    async def run_code(self):




        print("▶ Iniciando CodeAgent...")
        code_result = await self.agentcode.run()
        print("▶ CodeAgent finalizado.")


        return {
            "code_agent": code_result,
          
        }


class ConfiglogSCS:
    def __init__(self,   regras: str, tasklog: str):

        self.tasklog = tasklog

        self.regras = regras

        self.agent_log = CodeAgent(
            llm=ChatBrowserUse(),
            task=self.tasklog,
            rules=self.regras,
        )

    async def run_log(self, log_task: str):
        print("▶ Iniciando Agent Log...")
        log_result = await self.agent_log.run()
        print("▶ Agent Log finalizado.")
        return {
            "agent_log": log_result,
        }
    

