from fastapi import FastAPI

app = FastAPI()

# Home page
@app.get("/home")
def home():
    return 'Welcome to ESG Data & IA FastAPI Workshop'