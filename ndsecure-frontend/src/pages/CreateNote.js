import React, { useState } from "react";

const CreateNote = () => {
  const [note, setNote] = useState("");

  const handleCreateNote = () => {
    console.log("Note Created:", note);
  };

  return (
    <div>
      <h1>Create a New Note</h1>
      <textarea
        value={note}
        onChange={(e) => setNote(e.target.value)}
        placeholder="Write your note here..."
      />
      <button onClick={handleCreateNote}>Create Note</button>
    </div>
  );
};

export default CreateNote;
