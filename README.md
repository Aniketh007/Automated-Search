## Website: https://automated-search.streamlit.app/


# Automated Search Application

## Overview
This project is a web application built using Streamlit that allows users to perform a variety of operations on tabular data uploaded in CSV format. The application offers several features, including inserting, updating, deleting rows, and performing automated searches using Google Search API and OpenAI GPT for summarization. The tool is designed to help users manage datasets efficiently and retrieve contextual information based on the data entries.

## Features
### File Upload
- Users can upload CSV files, which are then displayed in the application.
- The table data is fully interactive with options to modify it through various operations.

### Data Operations
- **Search**: Retrieve information based on user queries
- **Insertion**: Add new rows to the dataset by entering values for each column.
- **Updation**: Modify specific cell values in any row based on the row index and column.
- **Deletion**: Remove rows from the dataset by specifying the row index.

### Automated Search
- **Search**: Users can perform searches based on the data in the selected column. The application fetches contextual information via Google Search API(SerpAPI) and generates summaries using OpenAI GPT.
- Results are displayed as a new table with the entity and corresponding summary.

## Demo
[![Watch the Demo](https://img.youtube.com/vi/XMximXjXYdI/0.jpg)](https://youtu.be/XMximXjXYdI?si=BW1_SbHu5rCaKKgn)

## Technologies Used
- **Streamlit**: A powerful Python framework to create interactive web applications.
- **Pandas**: For data manipulation and managing tabular data.
- **Google Search API**: For querying Google and retrieving search results related to specific entities.
- **OpenAI GPT (ChatGPT)**: For summarizing search results into concise and informative statements.
- **Python**: For API communication and handling responses.

---

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/automated-search-table-management.git
cd automated-search-table-management
```
### 2. Install Dependencies

To get started, you need to install the required Python dependencies. These dependencies include essential libraries for the application, such as `streamlit`, `pandas`, `openai`, and `requests`. Install them using the following command:

```bash
pip install -r requirements.txt
```
### 3. API Key Setup
- SearpAPI: I have used SerpAPI for content retrieval from web.
  - Go to the SeapAPI website(https://serpapi.com/users/sign_in)
  - Sign in to your account or create a new one if needed.
  - Browse the available plans and select the one that suits your requirements.
  - Copy the generated Private API Key from your account dashboard.
  - Paste this key into the application when prompted.
- OpenAI API: OpenAI API was used for summarization of extracted content.
  - Go to the OpenAI page(https://platform.openai.com)
  - Log in to your OpenAI account or create a new one.
  - Navigate to the API Keys section under your account settings.
  - Generate a new Secret API Key.
  - **Note**: Copy the API key immediately, as it will not be visible later.
  - Paste this API key into the application when prompted.
### 4. Enter the Query and Prompt
Once the application is running, follow these steps to perform a search and retrieve summarized results:

- Provide the Query:
  -Enter the entity, term, or topic you want to search for in the input field.
-Optional Prompt:
 - If desired, provide a specific prompt or context to guide the summarization.
 - If no custom prompt is provided, a default summarization prompt will be used.
- Run the Application:
  -Click on the Run button to initiate the search and summarization process.
### 5. Output
- The application will display the results in a table format. The output includes:
  - Entity Name: The search term or query.
  - Summary: A concise summary of the web content retrieved for the query.
- You can download the output in CSV format for further use by clicking on the Download button provided in the app.
