from fastapi import FastAPI

# create an instance of the FastAPI app
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World!"}

# to run the app go to terminal and write " uvicorn  main:app --reload"