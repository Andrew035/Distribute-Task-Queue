import logging
from celery import Celery
import time

# Configure loggin
logger = logging.getLogger(__name__)

# Connect to Redis
app = Celery("tasks", broker="redis://redis:6379/0")


@app.task(bind=True)
def heavy_computation(self, data):
    # Step 1: Initialize
    self.update_state(
        state="PROGRESS", meta={"current": 0, "total": 100, "phase": "Initializing"}
    )
    time.sleep(2)

    self.update_state(
        state="PROGRESS", meta={"current": 50, "total": 100, "phase": "Crunching Data"}
    )
    time.sleep(2)

    return f"Completed processing {data}"
