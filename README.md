# AI-Powered-Virtual-Health-Assistant-GenAI

This project is a virtual doctor application that uses Google's Generative AI and Gradio to analyze medical reports, provide personalized health advice, and offer various health-related functionalities. Users can either upload their medical reports in PDF format or paste the text directly to get a detailed analysis and health guidance.

## Features

- **Medical Report Analysis**: Upload a PDF or paste text to get an analysis of your medical report, including diagnosis, treatment recommendations, and lifestyle advice.
- **Symptom Checker**: Enter symptoms to get potential conditions and advice.
- **Personalized Diet Plan**: Generate a diet plan based on your medical report.
- **Personalized Exercise Plan**: Generate an exercise plan based on your medical report.
- **Medication Reminder**: Set reminders for your medications.
- **Health Education**: Get educational content on various health topics.

## Getting Started

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/sharmapacific/AI-Powered-Virtual-Health-Assistant-GenAI.git
    cd AI-Powered-Virtual-Health-Assistant-GenAI
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Configuration

1. Replace the placeholder in the code with your actual Google Generative AI API key:
    ```python
    api_key = '#####################'  # Replace with your actual API key
    genai.configure(api_key=api_key)
    ```

### Usage

1. Run the application:
    ```sh
    python app.py
    ```

2. Open the provided local URL in your web browser.

3. Use the interface to upload your medical report or paste the text directly to get personalized health advice.


## Example

Here's how the interface looks:

### Medical Report Analysis
- Upload a PDF or paste the text of your medical report.
- Get a detailed analysis including diagnosis, treatment, and lifestyle advice.

### Symptom Checker
- Enter symptoms to get potential conditions and advice.

### Personalized Diet Plan
- Generate a diet plan based on your medical report.

### Personalized Exercise Plan
- Generate an exercise plan based on your medical report.

### Medication Reminder
- Set reminders for your medications.

### Health Education
- Get educational content on various health topics.

## Deployment
The app is deployed on Hugging Face. You can access the deployed version [here](https://huggingface.co/spaces/sharmapacific/AI-Powered-Virtual-Health-Assistant).

## Acknowledgments

- Thanks to [Google Generative AI](https://developers.google.com/ai) for providing the API.
- [Hugging Face](https://huggingface.co/) for providing the deployment platform.
- Thanks to [Gradio](https://gradio.app) for the user interface framework.
