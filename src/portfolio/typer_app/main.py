from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check() -> dict[str,str]:
   return {"status":"ok"}

@app.get("/")
def table() -> dict[str,str]:
   return {"table":"Initialized"}
