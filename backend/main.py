from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Multi-Agent AI System Backend is running"}

# Placeholder for AI agent implementations and MCP server integration
