from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from paint_yourself_api.routes import routes
from paint_yourself_api.services.vgg_style_transfer import StyleTransfer


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(routes)
