from celery import Celery
import time

# Connect to Redis
app = Celery("tasks", broker="redis://redis:6379/0")


@app.task
def heavy_computation(data):
    time.sleep(5)  # Simulate a 5-second heavy job
    return f"Processed: {data}"
