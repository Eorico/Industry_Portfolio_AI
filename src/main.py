from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os

from models.models import Query
from repositories.repositories import Repositories
from services.services import ChatBotServices

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise ValueError("MONGO_URI not set in .env")

app = FastAPI(title="Eorico Gonzales Portfolio Chat Bot")

repo = Repositories(MONGO_URI)
bot_service = ChatBotServices(repo)

@app.post("/ask")
async def ask_portfolio(query: Query):
    try:
        answer = bot_service.chatbot_ask(query.question)
        return {"answer": answer }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    