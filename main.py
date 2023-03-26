from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "welcome to daily expense tracker api"}