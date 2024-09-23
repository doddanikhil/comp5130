import React from "react";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div>
      <h1>Welcome to NDSecure Note</h1>
      <Link to="/create-note">Create a New Note</Link>
    </div>
  );
};

export default Home;
