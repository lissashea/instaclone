import React from 'react';

function Grid({ posts }) {
  return (
    <div className="grid-container">
      {posts.map((post, index) => (
        <div className="grid-item" key={index}>
          <img src={post.image} alt="Post Image" width="200" height="200" />
        </div>
      ))}
    </div>
  );
}

export default Grid;
