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
      .post('http://127.0.0.1:800
