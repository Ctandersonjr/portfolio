from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check() -> dict:
   return {"status":"ok"}

@app.get("/")
def table() -> dict:
   return {"table":"Initialized"}
