import { useState } from "react";

import Sidebar from "./components/Sidebar";

import Dashboard from "./pages/Dashboard";
import Candidates from "./pages/Candidates";
import Jobs from "./pages/Jobs";
import Matching from "./pages/Matching";
import Analytics from "./pages/Analytics";

function App() {
  const [page, setPage] = useState("dashboard");

  return (
    <div style={{ display: "flex" }}>
      <Sidebar setPage={setPage} />

      <div style={{ flex: 1 }}>
        {page === "dashboard" && <Dashboard />}
        {page === "candidates" && <Candidates />}
        {page === "jobs" && <Jobs />}
        {page === "matching" && <Matching />}
        {page === "analytics" && <Analytics />}
      </div>
    </div>
  );
}

export default App;