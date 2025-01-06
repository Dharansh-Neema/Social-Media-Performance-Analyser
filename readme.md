# Social Media Performance Analysis using Langflow and DataStax

## 🚀 Demo

[Live Demo](https://social-media-performance-analyser.streamlit.app/)

## 📖 Project Description

The Social Media Performance Analysis project provides insightful analytics on social media posts using a Retrieval-Augmented Generation (RAG) flow. The project is trained on customized datasets and leverages Langflow for flow management while DataStax VectorDB is used for efficient vector-based data storage and retrieval.

## 📊 Dataset Features

- **Platform**: The social media platform where the post was made.
- **Post Type**: Type of content (Image, Video, Text).
- **Post Content**: The actual content of the post.
- **Post Timestamp**: The date and time when the post was made.
- **Likes**: Number of likes received.
- **Comments**: Number of comments received.
- **Shares**: Number of shares received.
- **Impressions**: Total views of the post.
- **Reach**: Total number of unique viewers.
- **Engagement**: Overall interaction level (likes, comments, shares).
- **Audience**: Target audience for the post.
- **Audience Interest**: Interests and preferences of the audience.

## 📈 Langflow Diagrams

- **Data Flow**: ![Data Flow](https://github.com/Dharansh-Neema/Social-Media-Performance-Analyser/blob/main/img/Data-flow.png)
- **Retrieval Flow**: ![Retrieval Flow](https://github.com/Dharansh-Neema/Social-Media-Performance-Analyser/blob/main/img/Reterival%20Flow.png)

## 🛠️ Setup Instructions

Follow these steps to set up and run the project locally:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Dharansh-Neema/Social-Media-Performance-Analyser
   cd Social-Media-Performance-Analyser
   ```

2. **Create a Virtual Environment and Install Dependencies:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # For MacOS/Linux
   # OR
   .\venv\Scripts\activate  # For Windows
   pip install -r requirements.txt
   ```

3. **Setup Streamlit Secrets:**
   Create a `.streamlit/secrets.toml` file and add the following parameters:

   ```plaintext
   APPLICATION_TOKEN="your_application_token"
   LANGFLOW_ID="your_langflow_id"
   FLOW_ID="your_flow_id"
   ```

4. **Run the Streamlit App:**
   ```bash
   streamlit run main.py
   ```

🎯 The app will be accessible locally at `http://localhost:8501/`
