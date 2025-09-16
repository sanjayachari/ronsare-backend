from fastapi import FastAPI
from app.api.v1.endpoints.user import router as users_router

app = FastAPI(title="Ronsare Core API")

# include your users router
app.include_router(users_router, prefix="/users", tags=["Users"])
