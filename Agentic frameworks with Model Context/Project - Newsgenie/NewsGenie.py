import os
import streamlit as st
from tavily import TavilyClient
from langchain_openai import ChatOpenAI
from datetime import datetime

# ==============================
# Load API Keys
# ==============================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not OPENAI_API_KEY:
    st.error("⚠ OPENAI_API_KEY is missing. Please set it in environment variables.")
    st.stop()

if not TAVILY_API_KEY:
    st.error("⚠ TAVILY_API_KEY is missing. Please set it in environment variables.")
    st.stop()

# ==============================
# Initialize Clients
# ==============================

client = TavilyClient(api_key=TAVILY_API_KEY)

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.7,
    api_key=OPENAI_API_KEY
)

# ==============================
# News Fetch Function
# ==============================
@st.cache_data(ttl=300)
def fetch_news(query):
    try:
        result = client.search(
            query=query,
            max_results=5,
            search_depth="advanced"
        )

        if not result or "results" not in result:
            return []

        return result["results"]

    except Exception as e:
        return f"News service temporarily unavailable. Please try again later.\nDetails: {str(e)}"

# ==============================
# Query Processing Logic
# ==============================

def process_query(user_input):
    user_input_lower = user_input.lower()

    try:
        # If user asks for news
        if "news" in user_input_lower or "latest" in user_input_lower:
            news_results = fetch_news(user_input)

            if isinstance(news_results, str):
                return news_results  # Error message from fetch_news

            if not news_results:
                return "No relevant news found for your query."

            formatted_news = ""
            for item in news_results:
                formatted_news += f"**{item.get('title','No Title')}**\n"
                formatted_news += f"{item.get('url','')}\n\n"

            return formatted_news

        # For general queries
        else:
            response = llm.invoke(user_input)
            return response.content

    except Exception as e:
        return f"⚠ Something went wrong while processing your request.\nError: {str(e)}"


# ==============================
# Streamlit UI
# ==============================

if "history" not in st.session_state:
    st.session_state.history = []

st.title("📰 NewsGenie: Your AI News Assistant")

user_input = st.text_area("Enter your query or ask for latest news:")

if st.button("Get Response"):
    if user_input.strip():
        response = process_query(user_input)

        st.subheader("NewsGenie Response:")
        st.write(response)

        st.session_state.history.append({
            "query": user_input,
            "response": response,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    else:
        st.warning("Please enter a query.")

st.write("## Session History")

if st.session_state.history:
    for item in st.session_state.history:
        st.write(f"**Query:** {item['query']}")
        st.write(f"**Response:** {item['response']}")
        st.write(f"**Time:** {item['timestamp']}")
        st.divider()
else:
    st.write("No history yet.")
