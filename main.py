from fastapi import FastAPI, requests
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse
from typing import Optional

app = FastAPI()

@app.get("/ping")
def ping():
    return JSONResponse({"message": "pong" }, status_code=200)
