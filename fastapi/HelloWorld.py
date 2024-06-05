from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello"}

@app.get("/{name}")
def read_root(name: str):
    return {"Hello": name}