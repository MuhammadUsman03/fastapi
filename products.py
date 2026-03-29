from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

products = [
    {
        "category_id": 1,
        "name": "Laptop",
        "description": "Core i7 16GB RAM",
        "price": 1200.50,
        "quantity": 10
    },
    {
        "category_id": 2,
        "name": "Smartphone",
        "description": "Android 128GB",
        "price": 500.00,
        "quantity": 25
    },
    {
        "category_id": 3,
        "name": "Headphones",
        "description": "Wireless Noise Cancelling",
        "price": 150.75,
        "quantity": 40
    },
    {
        "category_id": 4,
        "name": "Keyboard",
        "description": "Mechanical RGB Keyboard",
        "price": 80.00,
        "quantity": 30
    },
    {
        "category_id": 5,
        "name": "Mouse",
        "description": "Wireless Mouse",
        "price": 25.99,
        "quantity": 50
    },
    {
        "category_id": 6,
        "name": "Monitor",
        "description": "24-inch Full HD",
        "price": 200.00,
        "quantity": 15
    },
    {
        "category_id": 7,
        "name": "Chair",
        "description": "Ergonomic Office Chair",
        "price": 180.00,
        "quantity": 20
    },
    {
        "category_id": 8,
        "name": "Desk",
        "description": "Wooden Study Desk",
        "price": 250.00,
        "quantity": 12
    },
    {
        "category_id": 9,
        "name": "Printer",
        "description": "All-in-One Inkjet Printer",
        "price": 130.00,
        "quantity": 18
    },
    {
        "category_id": 10,
        "name": "Tablet",
        "description": "10-inch Android Tablet",
        "price": 300.00,
        "quantity": 22
    }
]

app = FastAPI()

# GET METHOD
@app.get("/product")
def get_product():
    return products

@app.get("/product/{id}")
def get_product(id: int):
    for product in products:
        if product["category_id"] == id:
            return product
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

# POST METHOD
class Product(BaseModel):
    category_id: int
    name: str
    description: str
    price: float
    quantity: int

@app.post("/product")
def create_product(product: Product):
    new_product = product.model_dump()
    products.append(new_product)
    return {"Message": "Product was added"}

# PUT METHOD
class ProductUpdate(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

@app.put("/product/{id}")
def update_product(id: int, product_update: ProductUpdate):
    for product in products:
        if product["category_id"] == id:
            product["name"] = product_update.name
            product["description"] = product_update.description
            product["price"] = product_update.price
            product["quantity"] = product_update.quantity
            return {"Message": "Product was updated"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

# DELETE METHOD
@app.delete("/product/{id}")
def delete_product(id: int):
    for product in products:
        if product["category_id"] == id:
            products.remove(product)
            return {"Message": "Product was deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")