from quart import Quart, request, jsonify
from quart_cors import cors
import json
from openai import AsyncOpenAI
import PyPDF2
import docx
import os
from openai import AsyncOpenAI

# Initialize Quart app
app = Quart(__name__)
app = cors(app, allow_origin="http://localhost:3000")  # Allow requests from frontend

# Initialize the OpenAI async client
aclient = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_text_from_pdf(file_path):
    """Extract text from a PDF file."""
    text = ""
    try:
        with open(file_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text()
    except Exception as e:
        text = f"Error reading PDF: {str(e)}"
    return text

def extract_text_from_docx(file_path):
    """Extract text from a DOCX file."""
    try:
        doc = docx.Document(file_path)
        return "\n".join([paragraph.text for paragraph in doc.paragraphs])
    except Exception as e:
        return f"Error reading DOCX: {str(e)}"

async def analyze_resume_with_ai(resume_text):
    """Use OpenAI GPT to analyze and parse the resume text."""
    try:
        system_prompt = (
            "You are a highly intelligent AI trained to parse resumes. Extract the following details:\n"
            "1. Full Name\n"
            "2. Contact Information (Email, Phone, LinkedIn)\n"
            "3. Summary/Objective\n"
            "4. Skills\n"
            "5. Education (Degree, School, Graduation Date)\n"
            "6. Work Experience (Job Titles, Companies, Dates, Key Achievements)\n"
            "7. Projects and Extracurriculars\n"
            "Provide the output as a structured JSON object."
        )

        response = await aclient.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": resume_text},
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error processing resume with AI: {str(e)}"

async def generate_interview_questions(parsed_data, position, company, job_description):
    """Generate interview questions based on resume and job details."""
    try:
        system_prompt = (
            "You are an AI specialized in creating interview questions. Using the following data:\n"
            "1. Parsed Resume Data\n"
            "2. Job Position\n"
            "3. Company Name\n"
            "4. Job Description (if provided)\n\n"
            "Generate a list of interview questions tailored to the candidate's resume and the specific job role."
        )

        user_input = {
            "Parsed Resume Data": parsed_data,
            "Job Position": position,
            "Company Name": company,
            "Job Description": job_description,
        }

        response = await aclient.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": json.dumps(user_input, indent=2)},
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating interview questions: {str(e)}"

@app.route('/upload-resume', methods=['POST'])
async def upload_resume():
    try:
        if 'file' not in await request.files:
            return jsonify({"error": "No file part in the request"}), 400

        file = (await request.files).get('file')
        position = (await request.form).get('position', '').strip()
        company = (await request.form).get('company', '').strip()
        job_description = (await request.form).get('job_description', '').strip()

        if not file:
            return jsonify({"error": "No file selected"}), 400

        # Log received data
        print(f"Received: Position={position}, Company={company}, Job Description={job_description}")

        file_path = f"/tmp/{file.filename}"
        await file.save(file_path)

        if file.filename.endswith('.pdf'):
            extracted_text = extract_text_from_pdf(file_path)
        elif file.filename.endswith('.docx'):
            extracted_text = extract_text_from_docx(file_path)
        else:
            return jsonify({"error": "Unsupported file type"}), 400

        # Combine all text inputs
        combined_text = f"Resume:\n{extracted_text}\n\nPosition: {position}\n\nCompany: {company}\n\nJob Description: {job_description}"

        # Parse the resume with AI
        ai_parsed_data = await analyze_resume_with_ai(combined_text)
        print("AI Parsed Data:", ai_parsed_data)  # Log parsed data

        # Generate interview questions
        interview_questions = await generate_interview_questions(ai_parsed_data, position, company, job_description)
        print("Generated Interview Questions:", interview_questions)  # Log generated questions

        return jsonify({
            "message": "Resume uploaded and processed successfully.",
            "parsed_data": json.loads(ai_parsed_data),  # Ensure JSON is properly parsed
            "interview_questions": interview_questions.split("\n")  # Split into list for frontend
        }), 200
    except Exception as e:
        print("Error:", str(e))  # Log error details
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
