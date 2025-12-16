from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_posts():
    return [{"title": "Post Exemplo", "content": "Em breve..."}]