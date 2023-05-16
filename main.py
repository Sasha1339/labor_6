from controller import Controller
from fastapi import FastAPI
import uvicorn

app = FastAPI()

controller = Controller()

if __name__ == '__main__':
        uvicorn.run("controller:app",host='localhost',port=5005,reload=True)