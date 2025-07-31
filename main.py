from fastapi import FastAPI, requests
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse
from typing import Optional

app = FastAPI()

@app.get("/hello")
def read_hello(name: str, is_teacher: bool):
    if is_teacher==True:
        return JSONResponse({"message": "Hello teacher " + name}, status_code=200)
    return JSONResponse({"message": "Hello " + name}, status_code=200)

class WelcomeRequest(BaseModel):
    name: str

@app.post("/welcome")
def welcome_user(request: WelcomeRequest):
    return {f"Bienvenue {request.name}"}
