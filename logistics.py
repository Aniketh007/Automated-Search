import os
from serpapi import GoogleSearch
from langchain_openai import ChatOpenAI

# Global variables for API keys
google_api = None

def set_api(google_key, openai_key):
    global google_api
    google_api = google_key
    os.environ["OPENAI_API_KEY"] = openai_key

def search_web(query: str) -> list:
    if not google_api:
        raise ValueError("Google API key is not set.")

    params = {
        "q": query,
        "api_key": google_api,
        "num": 5
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    snippets = []
    if "organic_results" in results:
        for result in results["organic_results"]:
            if "snippet" in result:
                snippets.append(result['snippet'])
    return ''.join(snippets)

def summarize(text):
    if "OPENAI_API_KEY" not in os.environ or not os.environ["OPENAI_API_KEY"]:
        raise ValueError("OpenAI API key is not set.")

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0,
        max_tokens=50,
        timeout=None,
        max_retries=2
    )
    message = [
        {"role": "system", "content": "You are a helpful assistant that summarizes the text into a single sentence."},
        {"role": "user", "content": text}
    ]

    ai_msg = llm.invoke(message)
    return ai_msg.content
