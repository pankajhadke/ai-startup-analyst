# How to Test the phaAI-gen Prototype

This guide provides instructions for accessing and testing the phaAI-gen prototype. The easiest way to test is by using the live demo link provided in the `README.md`. For a full technical evaluation, follow the steps below to set up and run the application locally in a Google Cloud Shell environment.


## Accessing Google Cloud Components

### Prerequisites

*   A Google Cloud project with a billing account.
*   Google Cloud Shell, which has the necessary tools pre-installed.

### API Setup

The prototype requires the **Cloud Vision API** and **Vertex AI API**. These APIs must be enabled in your project.

1.  **Enable APIs:** Run the following `gcloud` commands in your Cloud Shell terminal:

    ```sh
    gcloud services enable aiplatform.googleapis.com
    gcloud services enable vision.googleapis.com
    ```

2.  **Authentication:** No separate API keys are needed. Cloud Shell automatically handles authentication by using the credentials of your signed-in user.

### Important Links

*   **Live Prototype:** https://phaai-gen-1043984975656.asia-southeast1.run.app/

## Local Setup and Execution

### Step 1: Clone the Repository

Open Google Cloud Shell and run:

```sh
git clone https://github.com/pankajhadke/ai-startup-analyst.git
cd ai-startup-analyst

### Step 2: Set up the Python Environment
1.	Create and activate a virtual environment:
sh
python3 -m venv venv
source venv/bin/activate

2.	Install system dependencies: The pdf2image library requires poppler-utils.
sh
sudo apt-get update
sudo apt-get install poppler-utils

3.	Install Python dependencies:
sh
pip install -r requirements.txt


### Step 3: Run the Web UI
1.	Start the Flask server:
sh
python web.py

2.	Access the UI: Click the "Web Preview" button at the top of the Cloud Shell window and select "Preview on port 8080."

### Step 4. Testing the Application
1.	Input Data:
1.	Upload a pitch deck. The prototype accepts both JPG and PDF files.
2.	Adjust the "Sector," "Geography," and metrics fields as needed.
2.	Analyze: Click the "Analyze" button to trigger the workflow.
3.	Review the Output: The results will be displayed on a new page, showing a formatted deal note with the executive summary, benchmarking analysis, and risk assessment. 

### Step 5. Key Artifacts for Evaluation
You can inspect the following files to verify the prototype's inner workings:
•	web.py: The main Flask application that handles web requests.
•	app/ directory: Contains the modular Python functions for ingestion, analysis, benchmarking, and risk detection.
•	data/ directory: Contains the sample pitch deck and benchmark CSV.
•	deal_notes/ directory: Stores the generated JSON deal notes. 

