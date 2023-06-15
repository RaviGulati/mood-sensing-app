from fastapi import FastAPI, HTTPException
from starlette.responses import Response

# from app.db.models import UserAnswer
# from app.api import api
import uvicorn
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Mood Sensing App"}


uvicorn.run(app)