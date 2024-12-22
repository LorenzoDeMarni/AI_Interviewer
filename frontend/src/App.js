import React, { useState } from "react";
import UploadForm from "./components/UploadForm";
import QuestionsDisplay from "./components/QuestionsDisplay";
import Header from "./components/Header"; // Import Header
import Footer from "./components/Footer"; // Import Footer

function App() {
    const [questions, setQuestions] = useState([]); // State to hold questions

    return (
        <div>
            <Header /> {/* Use Header */}
            <main className="container">
                {/* Pass the callback to UploadForm */}
                <UploadForm onQuestionsGenerated={(newQuestions) => setQuestions(newQuestions)} />
                {/* Pass the questions to QuestionsDisplay */}
                <QuestionsDisplay questions={questions} />
            </main>
            <Footer /> {/* Use Footer */}
        </div>
    );
}

export default App;
