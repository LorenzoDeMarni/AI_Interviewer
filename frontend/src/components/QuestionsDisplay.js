import React from "react";

function QuestionsDisplay({ questions }) {
    if (!questions || questions.length === 0) return null;

    return (
        <div>
            <h2>Generated Interview Questions</h2>
            <ul>
                {questions.map((question, index) => (
                    <li key={index}>{question}</li>
                ))}
            </ul>
        </div>
    );
}

export default QuestionsDisplay;
