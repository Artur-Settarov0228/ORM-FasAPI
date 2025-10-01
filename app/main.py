from fastapi import FastAPI

from app.routers.users import router as products_router


app = FastAPI(title="Blog API")

app.include_router(products_router)

