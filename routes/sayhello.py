from fastapi import APIRouter
from pydantic import BaseModel
from requests import get
from middlewares.verify_token_route import VerifyTokenRoute

SayHello = APIRouter(route_class=VerifyTokenRoute)


@SayHello.post("/users/sayhello")
def SayHello():
    return "Este es el resultado del coigo"