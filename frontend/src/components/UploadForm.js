import React, { useState } from "react";

function UploadForm({ onQuestionsGenerated }) {
    const [file, setFile] = useState(null);
    const [position, setPosition] = useState("");
    const [company, setCompany] = useState("");
    const [jobDescription, setJobDescription] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!file || !position || !company) {
            alert("Please fill out all fields and upload a file.");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);
        formData.append("position", position);
        formData.append("company", company);
        formData.append("job_description", jobDescription);

        try {
            const res = await fetch("http://127.0.0.1:5000/upload-resume", {
                method: "POST",
                body: formData,
            });

            if (res.ok) {
                const data = await res.json();
                onQuestionsGenerated(data.interview_questions); // Pass questions to parent
            } else {
                alert("Failed to generate questions. Try again.");
            }
        } catch (err) {
            console.error("Error:", err);
            alert("An error occurred. Please try again later.");
        }
    };

    return (
        <div className="form-container">
            <form id="upload-form" onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label htmlFor="job-position" className="form-label">
                        Job Position
                    </label>
                    <input
                        type="text"
                        id="job-position"
                        className="form-control"
                        placeholder="Enter the job position"
                        value={position}
                        onChange={(e) => setPosition(e.target.value)}
                        required
                    />
                </div>
                <div className="mb-3">
                    <label htmlFor="company-name" className="form-label">
                        Company Name
                    </label>
                    <input
                        type="text"
                        id="company-name"
                        className="form-control"
                        placeholder="Enter the company name"
                        value={company}
                        onChange={(e) => setCompany(e.target.value)}
                        required
                    />
                </div>
                <div className="mb-3">
                    <label htmlFor="job-description" className="form-label">
                        Job Description
                    </label>
                    <textarea
                        id="job-description"
                        className="form-control"
                        rows="4"
                        placeholder="Add a detailed job description (optional)"
                        value={jobDescription}
                        onChange={(e) => setJobDescription(e.target.value)}
                    />
                </div>
                <div className="mb-3">
                    <label htmlFor="resume-upload" className="form-label">
                        Upload Resume
                    </label>
                    <input
                        type="file"
                        id="resume-upload"
                        className="form-control"
                        accept=".pdf,.doc,.docx"
                        onChange={(e) => setFile(e.target.files[0])}
                        required
                    />
                </div>
                <button type="submit" className="btn btn-primary w-100">
                    Upload and Generate
                </button>
            </form>
        </div>
    );
}

export default UploadForm;
