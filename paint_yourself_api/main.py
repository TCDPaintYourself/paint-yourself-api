from fastapi import FastAPI
from paint_yourself_api.routes import routes


app = FastAPI()


app.include_router(routes)
