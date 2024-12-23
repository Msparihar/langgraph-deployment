from fastapi import FastAPI
from app.routes import agent, chat


app = FastAPI()

app.include_router(agent.router)
app.include_router(chat.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
