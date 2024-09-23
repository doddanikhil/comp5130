import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import CreateNote from "./pages/CreateNote";
import ViewNote from "./pages/ViewNote";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/create-note" element={<CreateNote />} />
        <Route path="/view-note/:id" element={<ViewNote />} />
      </Routes>
    </Router>
  );
}

export default App;
