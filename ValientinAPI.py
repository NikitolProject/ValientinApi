from fastapi import FastAPI

from Valientin_API.routers import routers


app = FastAPI(title="Valientin API")


for api_router in routers:
  app.include_router(api_router)
