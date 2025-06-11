# AI Resume Critiquer
## A Brief Introduction
This project presents an AI-powered web application designed to provide constructive feedback on resumes. Built using Streamlit, it allows users to upload their resumes (in PDF or TXT format) and, optionally, specify a target job role. The application then leverages OpenAI's large language models to deliver a detailed analysis, helping users enhance their resume's clarity, impact, and overall effectiveness for their desired job applications.

## Features
* Resume Upload: Easily upload your resume, supporting both PDF and TXT file formats.

* Targeted Feedback: Get more relevant and tailored critique by optionally specifying a target job role.

* AI-Powered Analysis: Utilizes OpenAI's gpt-4o-mini model to provide detailed feedback on:

* Content clarity and impact

* Skills presentation

* Experience descriptions

* Specific improvements based on the provided job role.

* User-Friendly Interface: An intuitive and interactive web interface powered by Streamlit.

## Tech Stack
This project is primarily built with Python and integrates powerful AI and web development frameworks:

* Python: The core programming language. This project specifically requires Python 3.11 or higher.

* Streamlit: Used for building the interactive and user-friendly web interface.

* PyPDF2: Enables the application to read and extract text from PDF files.

* python-dotenv: Securely loads environment variables, such as API keys, from a .env file.

* OpenAI: Provides access to the advanced Large Language Models (LLMs), specifically gpt-4o-mini, for resume analysis.

* uv: A modern and fast Python package installer and resolver, used for efficient dependency management.

## APIs Used
OpenAI API: This project interacts with the OpenAI platform to utilize its gpt-4o-mini model, which performs the core resume analysis and critique.

## Installation & Setup
To get a local copy of this project up and running, follow these simple steps:

### Prerequisites
* Ensure you have Python 3.11 or higher installed on your system.

* An OpenAI API key.

### Installation
* Clone the Repository:

git clone <your-repository-url>
cd Resume-Critiquer # Or the directory where your project files are located

* Set up Virtual Environment and Install Dependencies:
This project uses uv for dependency management. If you don't have uv installed, you can install it via pip:

pip install uv

* Then, create a virtual environment and install the project dependencies:

uv venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
uv pip sync

(Note: pyproject.toml lists the direct dependencies, and uv.lock contains the locked versions of all dependencies. uv pip sync ensures all locked dependencies are installed for a consistent environment.)

* Environment Variables Setup
Create a file named .env in the root directory of your project (if it doesn't already exist) and add your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key_here

Replace your_openai_api_key_here with your actual API key obtained from the OpenAI Platform.

## Usage
Once installed and configured, you can run the AI Resume Critiquer from your terminal:

Run the Streamlit Application:
Ensure your virtual environment is active, then execute the main.py script using Streamlit:

streamlit run main.py

This command will automatically open the application in your default web browser, typically at http://localhost:8501.

* Upload Your Resume:
On the web interface, use the provided "Upload your resume (PDF or TXT)" button to select and upload your resume file.

* Enter Job Role (Optional):
If you have a specific job role in mind, type it into the "Enter the job role you're targetting (optional)" text box. This helps the AI provide more targeted and relevant feedback.

* Analyze Resume:
Click the "Analyze Resume" button. The application will process your resume, send it to the AI for analysis, and then display the comprehensive critique directly on the page.


Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please feel free to open an issue or submit a pull request.

License
This project is open-source.

Contact
Zaahir Sharma - sharma.zaahir@gmail.com - https://www.linkedin.com/in/zaahir-sharma/

Project Link: [[https://github.com/zaahirsharma/Resume-Critiquer](https://github.com/zaahirsharma/Resume-Critiquer)]
