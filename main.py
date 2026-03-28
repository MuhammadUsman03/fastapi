from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return{"Message": "Hello Usman Taj"}

@app.get("/greet")
def greeting():
    return{"Greeting": "Good Morning Usman!"}

@app.get("/profile")
def profile():
    return{
        "Name": "Maria Ali",
        "Father Name": "Ali Ahtesham",
        "D.O.B": "31-Dec-2004",
        "Age": 21,
        "Qualification": "MBBS Doctor"
    }

# Path Parameter
@app.get("/greet/{name}")
def greet_name(name: str):
    return{"Message": f"Hello {name}"}

@app.get("/age/{age}")
def age(age: int):
    return{"Message": f"Your age is {age}"}

#If we have more than one path parameter
@app.get("/fruitandveg/{fruits}")
def fruit_veg(fruit: str, veg:str):
    return{
        "Fruit": f"{fruit}",
        "Vegetable": f"{veg}"
    }

# Query parameter
@app.get("/profile/{name}")
def bio_data(name: str, age: int):
    return{
        "Name": f"{name}",
        "Age": f"{age}"
    }

# Use Optional
@app.get("/fruit/{fruit}")
def fruit_or_price(fruit: str, price: Optional[int] = None): # we can pass any value instead of None
    return{
        "Fruit": f"{fruit}",
        "Price": f"{price}"
    }

#If we have more than one query parameter
@app.get("/info")
def info(name: str, age:int):
    return{"Info": f"My name is {name} and I'm {age} years old"}

# HTTP Post Method
class Student(BaseModel):
    name: str
    age: int
    roll: int

@app.post("/create_student")
def create_student(student: Student):
    return{
        "Name": student.name,
        "Age": student.age,
        "Roll No.": student.roll
    }