import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [taskId, setTaskId] = useState(null);
  const [status, setStatus] = useState("Idle");

  // 1. Trigger the background task
  const startTask = async () => {
    const res = await axios.post("http://localhost:8000/process/?data=Hello");
    setTaskId(res.data.task_id);
    setStatus("Processing...");
  };

  // 2. Poll the status every 2 seconds if a task is running
  useEffect(() => {
    let interval;
    if (taskId && status !== "SUCCESS") {
      interval = setInterval(async () => {
        const res = await axios.get(
          `http://localhose:8000/task-status/${taskId}`,
        );
        setStatus(res.data.status);
        if (res.data.status === "SUCCESS") clearInterval(interval);
      }, 2000);
    }
    return () => clearInterval(interval);
  }, [taskId, status]);

  return (
    <div>
      <h1>Task Queue Dashboard</h1>
      <button onClick={startTask}>Trigger Heavy Job</button>
      <p>
        Status: <strong>{status}</strong>
      </p>
    </div>
  );
}

export default App;
