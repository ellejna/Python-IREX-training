from sys import exception

from pydantic import BaseModel, constr, conint, FieldSerializationInfo, field_validator
from typing import Optional

class Address(BaseModel):
    city: str
    address: str

class User(BaseModel):
    id: conint(gt=0) # greater than
    name: constr(min_length=2, max_length=100)
    age: int
    @field_validator("age")
    def age_must_be_positive(cls, v):
        if v<0:
            raise ValueError("Age must be positive")
        return v
    email: str
    ip: Address
try:
    user1 = User(id=1, name="John", age=20, email="username@gmail.com", address="123 Main Street")
    print(user1)
except Exception as e:
    print(e)
