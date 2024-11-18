import streamlit as st
import pandas as pd
from logistics import search_web, summarize, set_api

st.title("Automated Search")

# File uploader
fil = st.file_uploader("Upload the File", type='csv')
if fil:
    df=pd.read_csv(fil)
    st.write("File Uploaded")
    st.dataframe(df,width=600)


    options = [
        "None",
        "Insertion",
        "Deletion",
        "Updation",
        "Search"
    ]
    option = st.selectbox("Select an operation", options)

    if option == "Insertion":
        new_row = {}
        for column in df.columns:
            new_row[column] = st.text_input(f"Enter the value for {column}", key=f"{column}_input")
        if st.button("Add Row"):
            if all(new_row.values()):
                new_row_df = pd.DataFrame([new_row])
                df = pd.concat([df, new_row_df], ignore_index=True)
                st.success("Row added successfully!")
                st.table(df)
            else:
                st.error("Please fill all fields.")
    
    elif option == "Deletion":
        row_idx = st.number_input("Enter the row index to delete", min_value=0, max_value=len(df)-1, step=1)
        if st.button("Delete Row"):
            df = df.drop(df.index[row_idx]).reset_index(drop=True)
            st.success("Row deleted successfully!")
            st.table(df)

    elif option == "Updation":
        row_idx = st.number_input("Enter the row index to update", min_value=0, max_value=len(df)-1, step=1)
        col = st.selectbox("Select the column to update", df.columns)
        new_val = st.text_input(f"Enter the new value for {col}")
        if st.button("Update Row"):
            st.session_state.df.at[row_idx, col] = new_val
            st.success("Row updated successfully!")
            st.table(df)

    elif option == "Search":
        google_api = st.text_input("Enter your Google Search API key", type="password")
        openai_api = st.text_input("Enter your OpenAI API key", type="password")
        if google_api and openai_api:
            set_api(google_api, openai_api)
            st.success("API keys set successfully!")
            query = st.text_input("Provide the query to search about",
                                value="Find the email address of {value}")
            check=st.checkbox("Do you wish to provide the prompt?")
            if check:
                prompt=st.text_input("Enter the Prompt")
            if query:
                col = st.selectbox("Select the column to search", df.columns)
                if st.button("Run"):
                    with st.spinner('Processing...'):
                        results = []
                        
                        for entity in df[col]:
                            query_temp = query.format(value=entity)
                            snippets = search_web(query_temp)
                            llm_prompt = f"""
                                You are an AI assistant. A user asked the query: "{query_temp}".
                                The following text was retrieved from the web:
                                {snippets}

                                Based on the query, summarize the most relevant information from the web text in one concise sentence.
                                """
                            summary = summarize(llm_prompt)
                            results.append({"Entity":entity, "Summary": summary})
                        results_df = pd.DataFrame(results)
                        st.write("Search Results:")
                        st.table(results_df)
        else:
            st.warning("Please enter both API keys to proceed.")
