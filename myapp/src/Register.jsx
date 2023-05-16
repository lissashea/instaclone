import axios from 'axios';
import React, { useState } from 'react';

function getCSRFToken() {
  const csrfCookie = document.cookie.match(/csrftoken=([^ ;]+)/);
  return csrfCookie ? csrfCookie[1] : '';
}

function Register() {
  const [username, setUsername] = useState('');
  const [password1, setPassword1] = useState('');
  const [password2, setPassword2] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();

    const formData = {
      username: username,
      password1: password1,
      password2: password2,
    };

    axios
      .post('http://127.0.0.1:8000/register/', formData, {
        headers: {
          'X-CSRFToken': getCSRFToken(),
        },
      })
      .then(response => {
        // Handle successful registration
        console.log('User registered:', response.data);
      })
      .catch(error => {
        // Handle registration error
        console.error('Error:', error);
      });
  };

  return (
    <div>
      <h2>Register</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Username:
          <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
        </label>
        <label>
          Password:
          <input type="password" value={password1} onChange={(e) => setPassword1(e.target.value)} />
        </label>
        <label>
          Confirm Password:
          <input type="password" value={password2} onChange={(e) => setPassword2(e.target.value)} />
        </label>
        <button type="submit">Register</button>
      </form>
    </div>
  );
}

export default Register;
