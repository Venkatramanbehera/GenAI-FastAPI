from fastapi import FastAPI

app = FastAPI(title="GenAI Learning Hub")

@app.get("/")
def home():
    return {"message": "Welcome to Venkat's GenAI Learning API"}