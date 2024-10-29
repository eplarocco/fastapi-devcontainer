#!/usr/bin/env python3

from fastapi import Request, FastAPI
from typing import Optional
from pydantic import BaseModel
import pandas as pd
import json
import os

api = FastAPI()

@api.get("/")  # zone apex
def zone_apex():
    return {"Hello": "Hello API"}

@api.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@api.get("/customer/{idx}")
def get_customer(idx: int):
    # Read the data from the CSV file
    df = pd.read_csv("../customers.csv")
    # Filter the data based on the index
    customer = df.iloc[idx]
    return customer.to_dict()

@api.post("/get_payload")
async def get_payload(request: Request):
    response = await request.json() #capture data submitted into response object
    geo = response.get("geo")
    url = "https://maps.google.com/?q={geo}".format(geo=geo)
    
    
    
    #num1 = response.get("num1")
    #num2 = response.get("num2")
    #sum = num1 + num2
    #return {"sum":sum}


    #return await request.json() #return whatever is given in json format
