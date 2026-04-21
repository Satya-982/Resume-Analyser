import { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [jobDesc, setJobDesc] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!file || !jobDesc) {
      alert("Please upload resume and enter job description");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("job_desc", jobDesc);

    setLoading(true);
    setResult(null);

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/analyze",
        formData
      );

      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert("Error connecting to backend");
    }

    setLoading(false);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Resume Analyzer</h1>

      <input type="file" onChange={(e) => setFile(e.target.files[0])} />

      <br /><br />

      <textarea
        placeholder="Paste Job Description"
        value={jobDesc}
        onChange={(e) => setJobDesc(e.target.value)}
        rows={5}
        cols={40}
      />

      <br /><br />

      <button onClick={handleSubmit}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>

      {result && (
        <div>
          <h2>Match Score: {result.match_score}%</h2>
          <p>Matched Skills: {result.matched_skills.join(", ")}</p>
        </div>
      )}
    </div>
  );
}

export default App;