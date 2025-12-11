from fastapi import APIRouter
from endpoints import auth, users, posts

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(auth.router, prefix="/auth")
api_router.include_router(users.router, prefix="/users")
api_router.include_router(posts.router, prefix="/posts")