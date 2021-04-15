import sys, os
sys.path.append(os.path.abspath(".."))

import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from workhour.database import engine
from workhour import models
from workhour.controller import user
from workhour.dependency import create_default_data

models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# origins = ["*"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(user.router)

create_default_data()

@app.get("/")
async def root():
    return "Hello FastAPI"




if __name__ == '__main__':
	uvicorn.run("main:app", host='127.0.0.1', port=8000)
    # uvicorn.run("main:app", host='127.0.0.1', port=8000, workers=2)