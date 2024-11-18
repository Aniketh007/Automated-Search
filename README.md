# Automated Search and Table Management Application

## Overview
This project is a web application built using Streamlit that allows users to perform a variety of operations on tabular data uploaded in CSV format. The application offers several features, including inserting, updating, deleting rows, and performing automated searches using Google Search API and OpenAI GPT for summarization. The tool is designed to help users manage datasets efficiently and retrieve contextual information based on the data entries.

## Features
### File Upload
- Users can upload CSV files, which are then displayed in the application.
- The table data is fully interactive with options to modify it through various operations.

### Data Operations
- **Insertion**: Add new rows to the dataset by entering values for each column.
- **Updation**: Modify specific cell values in any row based on the row index and column.
- **Deletion**: Remove rows from the dataset by specifying the row index.

### Automated Search
- **Search**: Users can perform searches based on the data in the selected column. The application fetches contextual information via Google Search API and generates summaries using OpenAI GPT.
- Results are displayed as a new table with the entity and corresponding summary.

### Scrollable Tables
- All tables (uploaded data, modified data, and search results) are displayed in a scrollable format for better readability when the dataset grows larger.

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
