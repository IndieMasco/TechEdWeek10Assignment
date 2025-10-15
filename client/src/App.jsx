import { useState, useEffect } from "react";
import "./App.css";
import axios from "axios";

function App() {
  const [array, setArray] = useState([]);
  const [links, setLinks] = useState([]);

  const fetchAPI = async () => {
    const response = await axios.get("http://127.0.0.1:8080/users");
    setArray(response.data.users);
    setLinks(response.data.links);
  };

  useEffect(() => {
    fetchAPI();
  }, []);

  return (
    <>
      <h1>Learning Python</h1>

      <h2>Users</h2>
      {array.map((users, index) => (
        <div key={index}>
          <span>{users}</span>
          <br />
        </div>
      ))}

      <h2>Links</h2>
      {links.map((links, index) => (
        <div className="links" key={index}>
          <span>
            <a href={links}>{links}</a>
          </span>
          <br />
        </div>
      ))}
    </>
  );
}

export default App;
