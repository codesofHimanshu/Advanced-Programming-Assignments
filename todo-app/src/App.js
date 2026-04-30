//Create a simple React component that maintains a list of todos using useState.
//Allow the user to add a todo and display all added todos on the screen.
import React, { useState } from "react";

function App() {
  // State to store todo list
  const [todos, setTodos] = useState([]);

  // State for input field
  const [task, setTask] = useState("");

  // Function to add a new todo
  const addTodo = () => {
    if (task.trim() !== "") {
      setTodos([...todos, task]); // Add new task to list
      setTask(""); // Clear input field
    }
  };

  // Function to delete a todo
  const deleteTodo = (indexToDelete) => {
    const updatedTodos = todos.filter((_, index) => index !== indexToDelete);
    setTodos(updatedTodos);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Todo List App</h2>

      {/* Input Field */}
      <input
        type="text"
        value={task}
        placeholder="Enter a todo"
        onChange={(e) => setTask(e.target.value)}
      />

      {/* Add Button */}
      <button onClick={addTodo}>Add</button>

      {/* Display Todos */}
      <h3>Added Todos:</h3>

      <ul>
        {todos.map((todo, index) => (
          <li key={index}>
            {todo}

            {/* Delete Button */}
            <button
              onClick={() => deleteTodo(index)}
              style={{ marginLeft: "10px" }}
            >
              Remove
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
