import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import random

# --- Streamlit page config ---
st.set_page_config(
    page_title="PromptPie",
    page_icon="🧠",
    layout="wide"
)

# --- Load logo ---
logo = Image.open("logo.png")  # Replace with your logo file

# --- Sidebar with logo and app name ---
with st.sidebar:
    st.image(logo, width=160)
    st.markdown("<h2 style='text-align: center; color: #3b82f6;'>PromptPie</h2>", unsafe_allow_html=True)
    st.markdown("AI-Powered Prompt Generator for Creators and Brands ✨")

# --- Navigation bar ---
selected = option_menu(
    menu_title=None,
    options=["Home", "Features", "About"],
    icons=["house", "stars", "info-circle"],
    orientation="horizontal",
    default_index=0
)

# --- Prompt Generator Function ---
def generate_prompts(topic):
    categories = {
        "🔥 Hook Prompts": [
            "What nobody tells you about",
            "The truth behind",
            "3 ways to improve your"
        ],
        "💡 Insight Prompts": [
            "Hidden secrets of",
            "Stop doing this with",
            "Why you're failing at"
        ],
        "📈 Growth Prompts": [
            "How I scaled in",
            "My daily routine for",
            "Small changes that improved my"
        ]
    }

    hashtags = ["#PromptPie", "#AIContent", "#MarketingTips", "#BuildInPublic", "#ContentCreation"]
    all_outputs = {}

    for section, templates in categories.items():
        lines = []
        for temp in templates:
            lines.append(f"{temp} {topic}. {random.choice(hashtags)}")
        all_outputs[section] = lines

    return all_outputs

# --- Home Page ---
if selected == "Home":
    st.markdown("<h1 style='text-align: center;'>Welcome to PromptPie 🧠</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:18px;'>Craft AI-powered viral prompts to elevate your brand, content, and storytelling.</p>", unsafe_allow_html=True)
    st.markdown("")

    topic = st.text_input("🔍 Enter your topic (e.g., mindset, health, AI, etc.):")

    if topic:
        prompts = generate_prompts(topic)
        full_text = ""

        st.markdown("### 🎯 Your AI-Generated Prompts:")

        for section, lines in prompts.items():
            st.subheader(section)
            for i, line in enumerate(lines, 1):
                st.markdown(f"**{i}.** {line}")
                full_text += f"{i}. {line}\n"
            st.markdown("---")

        st.download_button(
            label="📥 Download All Prompts",
            data=full_text,
            file_name=f"{topic}_prompts.txt",
            mime="text/plain"
        )

# --- Features Page ---
elif selected == "Features":
    st.title("✨ Features of PromptPie")
    st.markdown("""
    - 🔥 Multi-category AI prompt generation  
    - 🧠 Creative + Insightful + Growth prompts  
    - 🏷️ Auto-included relevant hashtags  
    - 📥 One-click download feature  
    - 🖼️ Clean, responsive interface  
    """)

# --- About Page ---
elif selected == "About":
    st.title("📘 About PromptPie")
    st.markdown("""
    **PromptPie** is an AI-powered tool that helps creators, marketers, and solopreneurs generate high-impact prompts in seconds.

    It’s designed to help you:
    - 🧠 Create viral content ideas
    - ✍️ Overcome content block
    - 📈 Scale your brand presence

    **Made with ❤️ by** [Keshav Sharma](https://www.linkedin.com/in/keshav-sharma-b15270257/)
    """)

# --- Footer ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; font-size:16px;'>
        Made with ❤️ by <a href=https://www.linkedin.com/in/keshav-sharma-b15270257/" target="_blank" style="color:#3b82f6;"><strong>Keshav</strong></a>
    </div>
    """,
    unsafe_allow_html=True
)
