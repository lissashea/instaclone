import React from 'react';

function Home({ username, profilePicture }) {
  return (
    <div>
      <h2>Welcome, {username}!</h2>
      {profilePicture ? (
        <img src={profilePicture} alt="Profile Picture" />
      ) : (
        <p>No profile picture found.</p>
      )}
    </div>
  );
}

export default Home;
