import streamlit as st
from streamlit_option_menu import option_menu
import random

# --- Page Config ---
st.set_page_config(
    page_title="PromptPie",
    page_icon="🧠",
    layout="wide"
)

# --- Header with Logo Only ---
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        .header-container {
            display: flex;
            align-items: center;
            padding: 4px 16px;
            background-color: #f8f9fa;
            border-bottom: 1px solid #e5e5e5;
            height: 70px;
        }

        .header-container img {
            height: 150px;  /* ← Bigger logo */
            width: auto;
            margin: 0;
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

# --- Prompt Generator Logic ---
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
    st.title("Generate Your Prompt")

    topic = st.text_input("Enter a topic:", placeholder="e.g. digital marketing, fitness, AI...")

    prompts_output = ""

    if st.button("Generate Prompts"):
        if topic.strip() == "":
            st.warning("Please enter a topic to generate prompts.")
        else:
            st.subheader("➡️ Your AI-Generated Prompts")

            for i in range(5):
                data = generate_prompt(topic)
                block = f"""
<div style='font-size: 15px; line-height: 1.6;'>
    <span style='font-size: 18px; font-weight: bold; color: #2563eb;'>Prompt {i+1}</span><br><br>

    <span style='font-weight: bold;'>1. Prompt:</span> {data['prompt']}<br>
    <span style='font-weight: bold;'>2. Hook:</span> {data['hook']}<br>
    <span style='font-weight: bold;'>3. Hashtags:</span> {data['hashtags']}<br>
    <hr>
</div>
"""
                prompts_output += block
                st.markdown(block, unsafe_allow_html=True)

            # Download Button
            st.download_button(
                label="📥 Download Prompts (.txt)",
                data=prompts_output,
                file_name=f"{topic}_prompts.txt",
                mime="text/plain"
            )

elif selected == "Features":
    st.title("Features")
    st.markdown("""
    - 🧠 AI-powered prompt generation  
    - 🎯 Targeted hooks for engagement  
    - 🏷️ Auto-generated hashtags  
    - 💾 Download-ready format  
    - ✨ Built for creators, marketers, and brands
    """)

elif selected == "About":
    st.title("About PromptPie")
    st.markdown("""
    PromptPie is your creative assistant powered by AI.  
    Generate high-converting prompts in seconds with built-in hooks and hashtags.  
    Built with ❤️ by [Keshav Sharma](https://www.linkedin.com/in/keshav-sharma-xb)
    """)
