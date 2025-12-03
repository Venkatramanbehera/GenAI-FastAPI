from fastapi import FastAPI

from src.projects import doc_ingestion

app = FastAPI(title="GenAI Learning Hub")
app.include_router(doc_ingestion.router)

@app.get("/")
def home():
    return {"message": "Welcome to Venkat's GenAI Learning API"}