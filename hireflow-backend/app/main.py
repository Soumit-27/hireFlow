from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import db
from app.routes.auth_router import router

app = FastAPI()

# ✅ Simple CORS (allow your frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/test-db")
async def test_db():
    await db.test.insert_one({"message": "Mongo connected"})
    return {"status": "success"}