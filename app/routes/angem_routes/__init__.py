from fastapi import APIRouter

from app.routes.angem_routes import (
    lab1
)


router = APIRouter(prefix='/angem', tags=["angem"])
router.include_router(lab1.router)
