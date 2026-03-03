from fastapi import FastAPI
from app.routes.auth_router import router as auth_router


app = FastAPI(title="HireFlow Backend")

app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "HireFlow backend running"}

