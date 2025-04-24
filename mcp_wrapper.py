from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import httpx
from fastapi_mcp import FastApiMCP

app = FastAPI(title="Mean Calculator MCP Wrapper")

class Numbers(BaseModel):
    values: List[float]

@app.post("/calculate_mean", operation_id="calculate_mean")
async def calculate_mean(numbers: Numbers):
    """Proxy endpoint that forwards the request to the existing Mean Calculator API."""
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8000/mean", json=numbers.dict())
        return response.json()

# Initialize and mount the MCP server
mcp = FastApiMCP(app)
mcp.mount()
