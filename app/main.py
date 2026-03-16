from fastapi import FastAPI
app=FastAPI() #This creates the ASGI application.
# Everything attaches to this object:
# routes
# middleware
# dependencies
# events

@app.get("/")
def root():
    return {"message":"helloooooo api is running"}
