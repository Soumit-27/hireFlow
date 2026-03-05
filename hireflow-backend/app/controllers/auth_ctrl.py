from fastapi import HTTPException
from app.database import db
from app.schemas.auth import RegisterSchema, LoginSchema
from app.utils.security import verify_password, hash_password
from app.utils.security import verify_password, create_access_token


async def register_user(user: RegisterSchema):
    existing = await db.users.find_one({"email": user.email})
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    user_dict = user.model_dump()
    user_dict["password"] = hash_password(user.password)

    await db.users.insert_one(user_dict)

    return {
        "message": "Registration successful",
        "email": user.email,
        "role": user.role,
        "company_name": user.company_name
    }


async def login_user(user: LoginSchema):
    db_user = await db.users.find_one({"email": user.email})

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Create token
    token = create_access_token(
        data={
            "sub": db_user["email"],
            "role": db_user["role"]
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "email": db_user["email"],
        "role": db_user["role"]
    }