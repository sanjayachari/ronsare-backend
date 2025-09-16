from fastapi import FastAPI
from app.api.v1.endpoints.user import router as users_router

app = FastAPI(title="Ronsare Core API")

# Include your users router
app.include_router(users_router, prefix="/user", tags=["Users"])

# Sample root route
@app.get("/")
def read_root():
    return {"message": "Welcome to Ronsare Core API!"}
