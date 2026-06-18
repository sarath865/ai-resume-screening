import { useState } from "react";

function Login() {

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = async () => {

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/auth/login",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        email,
                        password
                    })
                }
            );

            const data = await response.json();

            alert(
                JSON.stringify(data)
            );

        } catch (error) {

            alert("Login Failed");
        }
    };

    return (
        <div
            style={{
                textAlign: "center",
                marginTop: "100px"
            }}
        >
            <h1>AI Resume Screening System</h1>

            <input
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) =>
                    setEmail(e.target.value)
                }
            />

            <br />
            <br />

            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) =>
                    setPassword(e.target.value)
                }
            />

            <br />
            <br />

            <button
                onClick={handleLogin}
            >
                Login
            </button>
        </div>
    );
}

export default Login;