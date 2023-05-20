from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    message = "Welcome to youtube to mp3 conerter!"
    return {"Message: ": message}
