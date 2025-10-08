from fastapi import FastAPI
from app.routers import users
from app.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

# Create Fastapi Server
app = FastAPI(
    title="Project-1",
    description="Phela Project practice keh liye",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message":"Welcome to first project"}


print("LLM V0.1 New Branch Added ")
print("hey how are you!!")