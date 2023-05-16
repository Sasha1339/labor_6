from fastapi import FastAPI, Body, File
from requests import Request
import uvicorn  
from data import Data
import xml.etree.ElementTree as ET
from service import Service
import logging

app = FastAPI()
service = Service()

@app.post("/data/post")
async def postData(contents = Body()): 
    service.parsing_xml(contents)
    logging.warning('2342')
    return contents


@app.get("/data/get")
async def getCurrent():
    return service.calculate()

if __name__ == '__main__':
    uvicorn.run("controller:app",host='localhost',port=5005,reload=True)

    
    
        


   