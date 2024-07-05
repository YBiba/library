from fastapi import FastAPI, Depends
import models
import schemas
from database import engine, Base, get_db
from sqlalchemy.orm import Session

app = FastAPI()

# Create table from models
models.Base.metadata.create_all(engine)

# Home page
@app.get("/home")
def home():
    return 'Welcome to ESG Data & IA FastAPI Workshop'

# Add new book
@app.post("/books")
def add_book(request: schemas.book, db: Session = Depends(get_db)):
    
    new_book = models.book (title = request.title,
                           author =  request.author,
                           description = request.description,
                           published_year = request.published_year,
                           publisher = request.publisher
                        )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book

# Retrieve a list of all books
@app.get("/books")
def get_book(db: Session = Depends(get_db)):
    return db.query(models.book).all()


# Add new book
@app.post("/users")
def add_user(request: schemas.User, db: Session = Depends(get_db)):
    
    new_user = models.User (name = request.name,
                           birthday =  request.birthday,
                           gender = request.gender,
                           email = request.email
                        )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# Retrieve a list of all books
@app.get("/user")
def get_user(db: Session = Depends(get_db)):
    return db.query(models.User).all()