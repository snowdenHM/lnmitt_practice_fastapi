from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    recovery_email : EmailStr
    password: str

class UserUpdate(BaseModel):
    recovery_email: EmailStr | None = None
    email: EmailStr | None = None
    password: str | None = None

class User(UserBase):
    id: int
    is_active: bool

    # model_config = {"from_attributes": True}
    class Config:
        from_attributes=True