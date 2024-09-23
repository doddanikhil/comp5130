import React from "react";
import { useParams } from "react-router-dom";

const ViewNote = () => {
  const { id } = useParams();

  console.log("Fetching note:", id);

  return (
    <div>
      <h1>View Note</h1>
      <p>Note ID: {id}</p>
    </div>
  );
};

export default ViewNote;
