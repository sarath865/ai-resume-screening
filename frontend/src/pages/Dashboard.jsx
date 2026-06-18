import { useEffect, useState } from "react";
import axios from "axios";

function Dashboard() {
    const [analytics, setAnalytics] = useState({
        total_candidates: 0,
        total_jobs: 0,
    });

    useEffect(() => {
        loadAnalytics();
    }, []);

    const loadAnalytics = async () => {
        try {
            const response = await axios.get(
                "http://127.0.0.1:8000/analytics/"
            );

            setAnalytics(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div style={{ padding: "30px" }}>
            <h1>AI Resume Screening Dashboard</h1>

            <div
                style={{
                    display: "flex",
                    gap: "20px",
                    marginTop: "30px",
                }}
            >
                <div
                    style={{
                        border: "1px solid white",
                        padding: "20px",
                        width: "250px",
                    }}
                >
                    <h2>Total Candidates</h2>
                    <h1>{analytics.total_candidates}</h1>
                </div>

                <div
                    style={{
                        border: "1px solid white",
                        padding: "20px",
                        width: "250px",
                    }}
                >
                    <h2>Total Jobs</h2>
                    <h1>{analytics.total_jobs}</h1>
                </div>

                <div
                    style={{
                        border: "1px solid white",
                        padding: "20px",
                        width: "250px",
                    }}
                >
                    <h2>System Status</h2>
                    <h1>Active</h1>
                </div>
            </div>
        </div>
    );
}

export default Dashboard;
