from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import statistics

app = FastAPI(title="Mean Calculator")

class Numbers(BaseModel):
    values: List[float]

@app.post("/mean", operation_id="calculate_mean")
async def calculate_mean(numbers: Numbers):
    mean_value = statistics.mean(numbers.values)
    return {"mean": mean_value}
  
