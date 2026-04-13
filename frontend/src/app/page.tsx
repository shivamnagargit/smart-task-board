'use client';
import { useEffect, useState } from 'react';

// This defines what a Task looks like in TypeScript
interface Task {
  id: number;
  title: string;
  description: string;
  status: string;
}

export default function Home() {
  const [tasks, setTasks] = useState<Task[]>([]);
  
  // WARNING: Put your actual EC2 Public IP address here!
  const BACKEND_URL = "http://3.236.103.177:8000/tasks/";

  // This function fetches the data from the Kitchen
  useEffect(() => {
    fetch(BACKEND_URL)
      .then((res) => res.json())
      .then((data) => setTasks(data))
      .catch((err) => console.error("Failed to fetch tasks:", err));
  }, []);

  return (
    <main className="min-h-screen bg-gray-50 p-10">
      <div className="max-w-3xl mx-auto">
        <h1 className="text-4xl font-extrabold text-gray-900 mb-8 text-center">
          🚀 Smart Task Board
        </h1>
        
        <div className="grid gap-4">
          {tasks.length === 0 ? (
            <p className="text-center text-gray-500">No tasks found. Is the kitchen running?</p>
          ) : (
            tasks.map((task) => (
              <div key={task.id} className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow">
                <div className="flex justify-between items-center mb-2">
                  <h2 className="text-xl font-bold text-gray-800">{task.title}</h2>
                  <span className="px-3 py-1 bg-blue-100 text-blue-800 text-sm font-medium rounded-full uppercase">
                    {task.status}
                  </span>
                </div>
                <p className="text-gray-600">{task.description}</p>
              </div>
            ))
          )}
        </div>
      </div>
    </main>
  );
}
