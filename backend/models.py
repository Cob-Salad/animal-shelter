from uuid import UUID
from pydantic import BaseModel



class Animal(BaseModel): 
    cats: int
    dogs: int

class Shelter(BaseModel):
    id: UUID
    name: str
    address: str
    animals: Animal


class ShelterRequest(BaseModel):
    name:str
    address: str
    animals: Animal

class ShelterResponse(BaseModel):
    id: UUID


