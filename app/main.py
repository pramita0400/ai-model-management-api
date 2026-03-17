from fastapi import FastAPI
from app.routers import model_router
app=FastAPI() #This creates the ASGI application.
# Everything attaches to this object:
# routes
# middleware
# dependencies
# events
app.include_router(model_router.router)
@app.get("/")
def root():
    return {"message":"helloooooo api is running"}
