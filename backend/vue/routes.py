# backend/pets/routes.py

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

vue_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@vue_router.get("/")
def root():
    return {"message": "hello it's vue"}


@vue_router.get("/item/{id}")
def get_item_id(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})
