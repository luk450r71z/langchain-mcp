import os
from dotenv import load_dotenv
from mymcp.client import main
import asyncio

# Carga variables del archivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

agent_response = asyncio.run(main(OPENAI_API_KEY))

print(agent_response)


