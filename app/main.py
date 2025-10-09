from fastapi import FastAPI,Depends,HTTPException
from app.routers import users
from app.database import engine, Base,get_db
from models.users import User
from schemas.users import UserCreate,UserUpdate,User,UserBase
from sqlalchemy.orm import Session

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


print("My Main File is running")

#CRUD Operations assignment 
#CREATE 
@app.post("/users/",response_model=UserCreate)
def create_user(user:UserCreate,db: Session=Depends(get_db)):
    db_user=User(**user.model_dump()) # in pydantic version 2 dict() is not used instead model_dump() is used
    db.add(db_user)
    db.commit()
    db.refresh(db_user) # to update this object with real values from the DB 
    return db_user

#READ 
@app.get("/users/{user_id}",response_model=User)
def read_user(user_id:id,db: Session=Depends(get_db)):
    user=db.query(User).filter(User.id==user_id).first() # SQL Query equivalent to: SELECT * FROM table_name WHERE <condition>
    if not user:
        raise HTTPException(status_code=404,detail=f"{user_id} not found")
    return user