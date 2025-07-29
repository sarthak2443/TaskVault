import { useState } from "react";
import API from "../api/axios";

interface CreateTaskProps {
  onTaskCreated: () => void;
}

const CreateTask: React.FC<CreateTaskProps> = ({ onTaskCreated }) => {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await API.post("/tasks", { title, description });
      alert("✅ Task Created!");
      setTitle("");
      setDescription("");
      onTaskCreated(); // Refresh task list
    } catch (err: any) {
      alert(err.response?.data?.msg || "❌ Error creating task");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white p-4 rounded shadow-md mb-6">
      <h2 className="text-xl font-semibold mb-3">Create New Task</h2>

      <input
        type="text"
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        className="border p-2 w-full mb-2 rounded"
        required
      />

      <textarea
        placeholder="Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        className="border p-2 w-full mb-2 rounded"
        rows={3}
        required
      />

      <button
        type="submit"
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Add Task
      </button>
    </form>
  );
};

export default CreateTask;
