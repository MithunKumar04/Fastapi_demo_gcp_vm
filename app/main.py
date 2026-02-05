from fastapi import FastAPI

app = FastAPI()


@app.get("/welcome")
def welcome():
    return "welcome"

@app.get("/hello/{name}")
def hello(name):
    return f"hello {name}"