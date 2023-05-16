import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Route, Routes } from 'react-router-dom';
import Grid from './Grid.jsx';
import Home from './Home.jsx';
import Register from './Register.jsx';
import UploadPhoto from './UploadPhoto.jsx';
import Login from './Login.jsx';
function App() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/grid/')
      .then(response => {
        console.log(response.data.posts); // Check the content of response.data.posts
        setPosts(response.data.posts);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }, []);

  return (
    <div>
      <main>
        <Routes>
          <Route path="/grid" element={<Grid posts={posts} />} />
          <Route path="/home" element={<Home />} />
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />
          <Route path="/upload" element={<UploadPhoto />} />
          {/* Other routes */}
        </Routes>
      </main>
    </div>
  );
}

export default App;
