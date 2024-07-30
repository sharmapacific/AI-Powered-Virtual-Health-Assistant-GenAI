import google.generativeai as genai
from langchain.prompts import PromptTemplate
import gradio as gr
import pdfplumber
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the API key
api_key = os.getenv('API_KEY')

# Configure the API key for Google's generative AI
genai.configure(api_key=api_key)

# Define the generative model
model = genai.GenerativeModel('gemini-pro')

# Function to extract text from a PDF file and generate a response
def retrieve_text_from_pdf(file_path):
    with open(file_path, 'rb') as f:
        pdf = pdfplumber.open(f)
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Function to analyze the text and generate a response
def process_text(text):
    prompt_template = PromptTemplate.from_template("""
    You are a virtual doctor. A patient has provided their medical report, and you need to assist them with their health journey.
    
    **Patient Instructions:**
    - Analyze the medical report.
    - Identify the patient's health issues.
    - Provide a comprehensive solution including:
        - Diagnosis of the problem.
        - Recommended treatments or remedies.
        - Suggested physical activities.
        - Habits to give up.
        - Fruits and foods to include in the diet.
    - Ensure the guidance is clear and actionable.
    
    **Medical Report:**
    ```
    {PDF_text}
    ```
    **Solution:**
    ```
    [Provide detailed analysis and recommendations here]
    ```"""
    )
    prompt = prompt_template.format(PDF_text=text)
    response = model.generate_content(prompt).text
    return response, text
    # formatted_text = f"Paste this text in the diet plan and exercise plan sections to generate the plans:\n\n{text}"
    # formatted_response = f"Report Explanations:\n\n{response}"
    # return formatted_response, formatted_text

# Function to handle both PDF upload and text input
def process_user_input(input_type, pdf_file=None, report_text=None):
    if input_type == "Upload PDF" and pdf_file is not None:
        text = retrieve_text_from_pdf(pdf_file.name)
    elif input_type == "Paste Text" and report_text is not None:
        text = report_text
    else:
        return "Please provide a valid input.", ""
    
    return process_text(text)

# Function to check symptoms
def assess_symptoms(symptoms):
    prompt = f"As a virtual doctor, please analyze the following symptoms and provide potential conditions:\n{symptoms}"
    response = model.generate_content(prompt).text
    return response

# Function to generate a diet plan based on the medical report
def develop_diet_plan(report_text):
    prompt = f"Based on the medical report, provide a Customized diet and nutrition plan:\n{report_text}"
    response = model.generate_content(prompt).text
    return response

# Function to generate an exercise plan based on the medical report
def develop_exercise_plan(report_text):
    prompt = f"Based on the medical report, provide a Customized exercise plan:\n{report_text}"
    response = model.generate_content(prompt).text
    return response

# Function to set medication reminders
def schedule_medication_reminder(medication, time):
    return f"Reminder set for {medication} at {time}."

# Function to provide health education content
def develop_health_content(topic):
    prompt = f"Provide educational content on the following health topic:\n{topic}"
    response = model.generate_content(prompt).text
    return response

# Define Gradio interfaces for each function
demo = gr.Interface(
    fn=process_user_input,
    inputs=[
        gr.Radio(["Upload PDF", "Paste Text"], label="Select Input Method", value="Upload PDF"),
        gr.File(label="Upload PDF"),
        gr.Textbox(label="Or Paste Report Text here", lines=10)
    ],
    outputs=[gr.Textbox(label="Report Analysis"), gr.Textbox(label="Copy and Paste this Medical Report Text in Diet/Exercise Plan Generation")],
    description="Discover Your Path to Well-being",
)   

present_symptom_checker = gr.Interface(
    fn=assess_symptoms,
    inputs=gr.Textbox(placeholder="Enter your symptoms, e.g., fever, cough, fatigue", lines=2),
    outputs=gr.Textbox(label="Potential Conditions"),
    description="Symptom Checker",
    examples=[
        ["fever, cough, fatigue"],
        ["headache, nausea, dizziness"]
    ]
)

present_diet_plan = gr.Interface(
    fn=develop_diet_plan,
    inputs=gr.Textbox(placeholder="Paste the copied medical report text here", lines=10),
    outputs=gr.Textbox(label="Customized Diet Plan"),
    description="Customized Diet Plan",
)

present_exercise_plan = gr.Interface(
    fn=develop_exercise_plan,
    inputs=gr.Textbox(placeholder="Paste the copied medical report text here", lines=10),
    outputs=gr.Textbox(label="Customized Exercise Plan"),
    description="Customized Exercise Plan",
)

present_medication_reminder = gr.Interface(
    fn=schedule_medication_reminder,
    inputs=[gr.Textbox(placeholder="Enter medication name", lines=1), gr.Textbox(placeholder="Enter time, e.g., 10:00 AM", lines=1)],
    outputs=gr.Textbox(label="Medication Reminder"),
    description="Set Medication Reminder",
)

present_health_education = gr.Interface(
    fn=develop_health_content,
    inputs=gr.Textbox(placeholder="Enter health topic, e.g., benefits of regular exercise", lines=2),
    outputs=gr.Textbox(label="Learning materials"),
    description="Health Education",
    examples=[
        ["benefits of regular exercise"]
    ]
)


# Define the title and tabbed interface
title = gr.Markdown("# AI-Powered Virtual Health Assistant")

tabs = gr.TabbedInterface(
    [demo, present_symptom_checker, present_diet_plan, present_exercise_plan, present_medication_reminder, present_health_education], 
    ["Medical Report Analysis", "Symptom Checker", "Diet Plan", "Exercise Plan", "Medication Reminder", "Health Education"]
)

# Set up the layout
def create_interface():
    with gr.Blocks() as app:
        title.render()  # Render the title
        tabs.render()   # Render the tabs
    return app

# Launch the application
app = create_interface()
app.launch(debug=True)

