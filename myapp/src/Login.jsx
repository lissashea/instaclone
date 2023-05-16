import React, { useState } from 'react';
import axios from 'axios';

function getCSRFToken() {
  const csrfCookie = document.cookie.match(/csrftoken=([^ ;]+)/);
  return csrfCookie ? csrfCookie[1] : '';
}

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    const csrftoken = getCSRFToken(); // Retrieve the CSRF token

    axios
      .post('http://127.0.0.1:8000/login/', { username, password }, {
        headers: {
          'X-CSRFToken': csrftoken,
        },
      })
      .then((response) => {
        // Handle successful login
        console.log(response.data);
      })
      .catch((error) => {
        // Handle login error
        setError('Invalid username or password');
      });
  };

  return (
    <div>
      <h2>Login</h2>
      {error && <p>{error}</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={handleUsernameChange}
          />
        </div>
        <div>
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={handlePasswordChange}
          />
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;
