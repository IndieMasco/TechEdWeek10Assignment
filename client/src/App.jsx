import { useState, useEffect } from "react";
import "./App.css";
import axios from "axios";

function App() {
  const [array, setArray] = useState([]);

  const fetchAPI = async () => {
    const response = await axios.get("http://127.0.0.1:8080/api/users");
    setArray(response.data.users);
  };

  useEffect(() => {
    fetchAPI();
  }, []);

  return (
    <>
      <h1>Learning Python</h1>
      {array.map((users, index) => (
        <div key={index}>
          <span>{users}</span>
          <br />
        </div>
      ))}
    </>
  );
}

export default App;
