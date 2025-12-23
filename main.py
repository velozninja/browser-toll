from browser_use import Browser, Agent, CodeAgent, ChatBrowserUse
import dotenv
import os
import asyncio

apikey = "bu_97Y8Lb7xHIQyZoc-urORIOORDbh1NDGBPDy6j_FyrvI"

task ="1 encontrar dados a respeito do clima ou seja chuva e umidade no estado de Mato Grosso do Sul" \
       "2 analisar os dados encontrados e extrair informações relevantes sobre padrões de chuva e umidade" \
       "3 apresentar as informações de forma clara e concisa, destacando tendências e variações" \
       "4 fornecer informações de 2020 até 2025"


browser = Browser(headless=False)
bragent = Agent(
    browser=browser,
    task=task,
    llm=ChatBrowserUse(api_key=apikey)
)

async def main():
    result = await bragent.run()
    taskcd = "faça um grafico de barras com os dados das informações de tacha de chuva e umidade por data fornecida pela pesquisa nos dados da variavel result "
    agentcd = CodeAgent(
        task=taskcd,
        llm=ChatBrowserUse(api_key=apikey)
    )
    code_result = await agentcd.run()
    print(result)
    print(code_result)

asyncio.run(main())