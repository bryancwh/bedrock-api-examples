# bedrock-api-examples

This README provides instructions on how to configure Bedrock APIs and run a Streamlit application.

## Prerequisites

- Python 3.7 or higher
- pip3 (Python package installer)

## Setup

1. Clone the repository:

```
git clone https://github.com/bryancwh/bedrock-api-examples.git
cd bedrock-api-examples
```

2. (Optional) Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

3. Install the required dependencies:

```
pip3 install -r requirements.txt
```

## Running the Application

After installing the dependencies, you can run the Streamlit application using the following command:

```
streamlit run bedrock-kb.py
```

The application should now be running. Open a web browser and go to the URL displayed in your terminal (usually `http://localhost:8501`).

## Troubleshooting

If you encounter any issues:

1. Ensure all dependencies are correctly installed.
2. Check that you're using a compatible Python version.
3. Verify that the Bedrock parameters in Streamlit scripts have been replaced (e.g., `knowledgeBaseId = YOUR_BEDROCK_KB_ID`)

For more information, refer to the [Streamlit documentation](https://docs.streamlit.io/).