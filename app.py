import streamlit as st
from streamlit_option_menu import option_menu
import random

# --- Page configuration ---
st.set_page_config(
    page_title="PromptPie",
    page_icon="🧠",
    layout="wide"
)

# --- Custom HTML Header with Logo ---
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: visible;}

        .header-container {
            display: flex;
            align-items: center;
            padding: 12px 16px;
            background-color: #f8f9fa;
            border-bottom: 1px solid #e5e5e5;
        }

        .header-container img {
            height: 120px;
            max-height: 120px;
        }
    </style>

    <div class="header-container">
        <a href="https://www.linkedin.com/in/keshav-sharma-xb" target="_blank">
            <img src="https://raw.githubusercontent.com/Keshav-xb/PromptPie/main/logo.png" alt="PromptPie Logo">
        </a>
    </div>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.markdown("### Welcome to PromptPie")
    st.write("🚀 AI-Powered Prompt Generator for Creators and Brands.")
    st.write("📌 Built with ❤️ by [Keshav Sharma](https://www.linkedin.com/in/keshav-sharma-xb)")

# --- Navigation ---
selected = option_menu(
    menu_title=None,
    options=["Home", "Features", "About"],
    icons=["house", "stars", "info-circle"],
    orientation="horizontal"
)

# --- Prompt Generator Function ---
def generate_prompt(topic):
    hooks = [
        f"Unlock the secret to {topic}",
        f"Why everyone is talking about {topic}",
        f"How to master {topic} in 3 easy steps",
        f"The hidden truth behind {topic}",
        f"Stop scrolling if you want to learn {topic}"
    ]
    hashtags = [
        f"#{topic.replace(' ', '')}",
        "#PromptPie",
        "#AIGenerated",
        "#ContentCreation",
        "#DailyPrompts"
    ]
    return {
        "prompt": f"Create a viral content piece about {topic}",
        "hook": random.choice(hooks),
        "hashtags": " ".join(random.sample(hashtags, 3))
    }

# --- Main Content ---
if selected == "Home":
    st.title("Prompt Generator")

    topic = st.text_input("Enter a topic:", placeholder="e.g. digital marketing, fitness, AI...")

    if st.button("Generate Prompts"):
        if topic.strip() == "":
            st.warning("Please enter a topic to generate prompts.")
        else:
            st.subheader("🎯 Your AI-Generated Prompts")
            for i in range(5):
                data = generate_prompt(topic)
                st.markdown(f"""
                **Prompt {i+1}:** {data['prompt']}  
                **Hook:** {data['hook']}  
                **Hashtags:** {data['hashtags']}
                ---
                """)

elif selected == "Features":
    st.title("Features")
    st.markdown("""
    - 🧠 AI-powered prompt generation
    - 🎯 Targeted hooks for engagement
    - 🏷️ Auto-generated hashtags
    - 💾 Easy copy/paste usage
    - ✨ Built for creators, marketers, influencers
    """)

elif selected == "About":
    st.title("About PromptPie")
    st.markdown("""
    PromptPie is your creative assistant — powered by AI — that helps you generate high-quality content prompts in seconds.  
    Created with 💙 by [Keshav Sharma](https://www.linkedin.com/in/keshav-sharma-xb)
    """)