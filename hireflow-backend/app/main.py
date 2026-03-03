
from fastapi import FastAPI
from app.database import db
from app.routes.auth_router import router

app = FastAPI()

app.include_router(router)

@app.get("/test-db")
async def test_db():
    await db.test.insert_one({"message": "Mongo connected"})
    return {"status": "success"}