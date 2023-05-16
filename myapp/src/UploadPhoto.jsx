import React from 'react';

function UploadPhoto({ form, handleSubmit }) {
  return (
    <div>
      <h2>Upload Photo</h2>
      <form onSubmit={handleSubmit} encType="multipart/form-data">
        {form}
        <button type="submit">Upload</button>
      </form>
    </div>
  );
}

export default UploadPhoto;
