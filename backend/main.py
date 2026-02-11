from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tasks import heavy_computation

app = FastAPI()


async def root(data: str):
    # .delay() sends the task to Redis and returns immediately
    task = heavy_computation.delay(data)
    return {"task_id": task.id, "status": "Processing in background..."}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
