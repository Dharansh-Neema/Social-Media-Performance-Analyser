import streamlit as st
import requests

# Load secrets 
APPLICATION_TOKEN = st.secrets["APPLICATION_TOKEN"]
LANGFLOW_ID = st.secrets["LANGFLOW_ID"]
FLOW_ID = st.secrets["FLOW_ID"]
# Langflow API settings
BASE_API_URL = "https://api.langflow.astra.datastax.com"

# Custom CSS for styling
st.markdown("""
    <style>
    .conversation-box {
        background-color: #FFFFFF;
        border: 1px solid #E0E0E0;
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .user-message {
        background-color: #E8F0FE;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        font-size: 18px;
        color: #2C3E50;
    }
    .ai-message {
        background-color: #F0F8FF;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        font-size: 18px;
        color: #34495E;
    }
    .chat-timestamp {
        font-size: 12px;
        color: #666;
        margin-top: 5px;
        text-align: right;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

def run_flow(message: str):
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{FLOW_ID}"
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat"
    }
    headers = {"Authorization": f"Bearer {APPLICATION_TOKEN}", "Content-Type": "application/json"}

    response = requests.post(api_url, json=payload, headers=headers)
    try:
        response_json = response.json()
        outputs_list = response_json.get("outputs", [])
        
        if outputs_list and "outputs" in outputs_list[0]:
            result = outputs_list[0]["outputs"][0].get("results", {}).get("message", {})
            text_response = result.get("text", "No text found in the response.")
        else:
            text_response = "Invalid response format received from the server."

        return text_response
    except Exception as e:
        return f"Error parsing response: {e}"

# Title
st.title("📊 Social Media Performance Analysis Chatbot")
st.markdown("""
    <div style='font-size: 18px; color: #666; margin-bottom: 30px;'>
        Ask questions about your social media post performance.
    </div>
""", unsafe_allow_html=True)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input section with improved styling
user_input = st.text_input("Enter your query here:", 
                          key="user_input",
                          placeholder="Type your question...")

# Handle user input and display chat history
if st.button("Analyze", key="analyze_button"):
    if user_input:
        # Get the response first
        response_message = run_flow(user_input)
        
        # Add both messages as a pair to chat history
        st.session_state.chat_history.insert(0, {
            "user_message": user_input,
            "ai_message": response_message,
            "timestamp": "Just now"
        })

        # Clear input box after sending the message
        st.rerun()

# Display chat history in reverse order with improved styling
for i, conversation in enumerate(st.session_state.chat_history):
    st.markdown(f"""
        <div class='conversation-box'>
            <div class='user-message'>
                <strong>You</strong><br>
                {conversation["user_message"]}
            </div>
            <div class='ai-message'>
                <strong>AI</strong><br>
                {conversation["ai_message"]}
            </div>
            <div class='chat-timestamp'>{conversation["timestamp"]}</div>
        </div>
    """, unsafe_allow_html=True)

#Footer note
