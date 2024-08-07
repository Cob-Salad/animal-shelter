# Make the pydantic model `Shelter` that will represent this data, then manually
# change this list to be a list[Shelter]. You don't need to write code to convert
# this list, just manually change it by hand.
from models import Shelter, Animal
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    )






shelters: list = [
    Shelter(
        name = "St. George Animal Shelter",
        address = "605 Waterworks Dr, St. George, UT 84770",
        animals = Animal(cats = 13, dogs = 15)
        ),
    Shelter(
        name = "St. George Paws",
        address = "1125 W 1130 N, St. George, UT 84770",
        animals = Animal(cats = 12, dogs = 9)
    ),
    Shelter(
        name = "Animal Rescue Team",
        address = "1838 W 1020 N Ste. B, St. George, UT 84770",
        animals = Animal(cats = 4, dogs = 7)
    ),
        Shelter(
        name = "cob salads rescue",
        address = "45 north 500 east, st george, 84770",
        animals = Animal(cats = 9, dogs = 7)
    )
]







@app.get("/shelters")
async def list_shelters() -> list[Shelter]:
    return shelters

@app.post("/shelters")
async def create_shelter(shelter: Shelter):
    shelters.append(shelter)

@app.put("/shelters/{name}")
async def update_shelter(updatedShelter: Shelter, name: str):
    for i, index in enumerate(shelters):
        if index.name == name:
            shelters[i] = updatedShelter
            return
        else:
            shelters.append(updatedShelter)
            return


@app.delete("/shelters/{name}")
async def delete_shelter(name: str):
    for i, index in enumerate(shelters):
        if index.name == name: 
            shelters.pop(i)
            return
