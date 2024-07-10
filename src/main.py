from fastapi import FastAPI
from database import InMemoryDatabase

import uvicorn


app = FastAPI()


@app.get("/health", status_code=200, tags=["health"], summary="Health check")
async def health():
    return {"status": "ok"}

@app.post("/user/", tags=["example"], summary="Insert user")
async def insert(data: dict):
    db = InMemoryDatabase()
    users = db.get_collection('users')
    users.insert_one(data)
    return {"status": "ok"}

@app.get("/user/{name}", status_code=200, tags=["example"], summary="Get user by name")
async def get(name: str):
    db = InMemoryDatabase()
    users = db.get_collection('users')
    user = users.find_one({"name": name})
    return {"status": "ok", "user": user}

@app.get("/user/", tags=["example"], summary="List all users")
async def list():
    db = InMemoryDatabase()
    users = db.get_collection('users')
    return {"status": "ok", "users": [x for x in users.find({},{"_id": 0})]}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="debug")