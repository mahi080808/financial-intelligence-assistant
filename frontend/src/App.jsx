import { useState } from "react";
import "./App.css";

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [status, setStatus] = useState("");
  const [loading, setLoading] = useState(false);

  const uploadPDF = async () => {
    if (!selectedFile) {
      alert("Please select a PDF first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    setStatus("Uploading PDF...");

    const response = await fetch("http://127.0.0.1:8000/upload", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    setStatus(data.message);
  };

  const askAI = async () => {
    if (!question) return;

    setLoading(true);

    const response = await fetch(
      `http://127.0.0.1:8000/ask?question=${encodeURIComponent(question)}`,
      {
        method: "POST",
      }
    );

    const data = await response.json();

    setAnswer(data.answer);

    setLoading(false);
  };

  return (
    <div className="container py-5">

      <div className="card shadow-lg p-4">

        <h1 className="text-center mb-4">
          🤖 Financial Intelligence Assistant
        </h1>

        <div className="mb-4">

          <h4>📄 Upload PDF</h4>

          <div className="d-flex gap-3">

            <input
              type="file"
              className="form-control"
              onChange={(e) => setSelectedFile(e.target.files[0])}
            />

            <button
              className="btn btn-primary"
              onClick={uploadPDF}
            >
              Upload
            </button>

          </div>

          <p className="text-success mt-3">
            {status}
          </p>

        </div>

        <hr />

        <div className="mb-4">

          <h4>💬 Ask AI</h4>

          <div className="d-flex gap-3">

            <input
              type="text"
              className="form-control"
              placeholder="Ask anything about the uploaded PDF..."
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
            />

            <button
              className="btn btn-success"
              onClick={askAI}
            >
              Ask AI
            </button>

          </div>

        </div>

        <hr />

        <h4>🤖 AI Response</h4>

        <div className="answer-box">

          {loading ? (
            <div className="text-center">

              <div
                className="spinner-border text-primary"
                role="status"
              >
              </div>

              <p className="mt-3">
                Thinking...
              </p>

            </div>
          ) : (
            answer || "Ask a question to begin..."
          )}

        </div>

      </div>

    </div>
  );
}

export default App;