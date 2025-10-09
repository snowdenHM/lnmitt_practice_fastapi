from fastapi import FastAPI,Depends,HTTPException
from app.routers import users
from app.database import engine, Base,get_db
from app.models.users import User as UserModel
from app.schemas.users import UserCreate,UserUpdate,User as UserSchema
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
@app.post("/users/",response_model=UserSchema)
def create_user(user:UserSchema,db: Session=Depends(get_db)):
    db_user=UserModel(**user.model_dump()) # in pydantic version 2 dict() is not used instead model_dump() is used
    db.add(db_user)
    db.commit()
    db.refresh(db_user) # to update this object with real values from the DB 
    return db_user

#READ 
@app.get("/users/{user_id}",response_model=UserSchema)
def read_user(user_id:int,db: Session=Depends(get_db)):
    user=db.query(UserModel).filter(UserModel.id==user_id).first() # SQL Query equivalent to: SELECT * FROM table_name WHERE <condition>
    if not user:
        raise HTTPException(status_code=404,detail=f"{user_id} not found")
    return user

#UPDATE 
@app.put("/users/{user_id}",response_model=UserSchema)
def update_user(user_id:int,db_update:UserUpdate,db:Session=Depends(get_db)):
    db_user=db.query(UserModel).filter(UserModel.id==user_id).first()
    if not db_user:
        raise HTTPException(status_code=404,detail=f"{user_id} no such id exists")
    
    update_data= db_update.model_dump(exclude_unset=True) # As our UserUpdate schema has default value to NONE 
    #only updates what user actually wants to
    for key,value in update_data.items():
        setattr(db_user,key,value)

    db.commit()
    db.refresh(db_user)
    return db_user    

#DELETE 