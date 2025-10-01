from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    first_name: str 
    last_name: str 
    username: str 
    gender: str 
    phone: str 

    class Config:
        from_attributes = True
        