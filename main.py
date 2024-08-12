from fastapi import FastAPI
from dotenv import load_dotenv
from routes.auth import auth_routes
from routes.sayhello import SayHello
app = FastAPI()

app.include_router(auth_routes, prefix="/api")
app.include_router(SayHello, prefix="/api")
load_dotenv()