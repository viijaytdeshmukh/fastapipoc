from fastapi import FastAPI

app = FastAPI()

@app.get("/data")
async def get_data():
    return {"message": "Hello from my laptop!", "data": [1, 2, 3, 4]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
