function Sidebar({ setPage }) {
  return (
    <div
      style={{
        width: "250px",
        height: "100vh",
        background: "#111827",
        color: "white",
        padding: "20px",
      }}
    >
      <h2>AI Resume Screening</h2>

      <hr />

      <button onClick={() => setPage("dashboard")}>
        Dashboard
      </button>

      <br />
      <br />

      <button onClick={() => setPage("candidates")}>
        Candidates
      </button>

      <br />
      <br />

      <button onClick={() => setPage("jobs")}>
        Jobs
      </button>

      <br />
      <br />

      <button onClick={() => setPage("matching")}>
        AI Matching
      </button>

      <br />
      <br />

      <button onClick={() => setPage("analytics")}>
        Analytics
      </button>
    </div>
  );
}

export default Sidebar;