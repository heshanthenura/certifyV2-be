import config

from fastapi import FastAPI
from routers import admin, certificate

app = FastAPI()

app.include_router(admin.router, prefix="/api")
app.include_router(certificate.router, prefix="/api")
