import { useState, useEffect } from "react";
import API from "../api/axios";

interface Task {
  id: number;
  title: string;
  description: string;
  completed: boolean;
  created_at: string;
}

const Dashboard = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  const fetchTasks = async () => {
    const res = await API.get("/tasks");
    setTasks(res.data);
  };

  const createTask = async () => {
    if (!title.trim()) return;
    await API.post("/tasks", { title, description });
    setTitle("");
    setDescription("");
    fetchTasks();
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <div className="p-6 max-w-3xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Dashboard</h1>

      <div className="mb-6">
        <input
          type="text"
          placeholder="Title"
          className="border p-2 w-full mb-2 rounded"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <textarea
          placeholder="Description"
          className="border p-2 w-full mb-2 rounded"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        ></textarea>
        <button
          onClick={createTask}
          className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
        >
          Add Task
        </button>
      </div>

      <div>
        {tasks.map((task) => (
          <div
            key={task.id}
            className="bg-white p-4 mb-2 rounded shadow-md"
          >
            <h3 className="font-semibold">{task.title}</h3>
            <p>{task.description}</p>
            <p className="text-xs text-gray-500">Created: {task.created_at}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Dashboard;