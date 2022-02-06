from fastapi import APIRouter
from paint_yourself_api.routes import styled_images


routes = APIRouter()


routes.include_router(
    styled_images.router, prefix="/styled-images", tags=["styled-images"]
)
