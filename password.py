import streamlit as st
import re

# Set page config
st.set_page_config(page_title="Password Generator", page_icon="🔐")
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/premium-vector/cybersecurity-information-network-protection-future-technology-web-services-business-internet-project_118331-1189.jpg?w=1060");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    </style>
""", unsafe_allow_html=True)

# App title and description
st.markdown("""
<h1 style='
    text-align: center;
    font-size: 60px;
    color:#f63366;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    font-family: Arial, sans-serif;
'>
 Password Generator
</h1>
""", unsafe_allow_html=True)
st.markdown("""
<h2 style='
    text-align: center;
    color: #333333;
    font-size: 32px;
    margin-top: 20px;
    margin-bottom: 10px;
'>
🎉 Welcome to the <span style="color:#003566;">Ultimate Password Generator!</span>
</h2>
<p style='
    text-align: center;
    color: #555555;
    font-size: 18px;
    margin-bottom: 30px;
'>
Use this tool to generate a <b>strong password</b> for your accounts and stay secure online.
</p>
""", unsafe_allow_html=True)


# Password input
password = st.text_input("Enter your password", type="password")

# Feedback and scoring
feedback = []
score = 0

if password:
    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be at least 8 characters long.")
    
    # Check for upper and lower case letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password must contain both uppercase and lowercase letters.")
    
    # Check for numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password must contain at least one number.")
    
    # Check for special characters (fixed space issue)
    if re.search(r"[!#@%&]", password):
        score += 1
    else:
        feedback.append("❌ Password must contain at least one special character (!, #, @, %, &).")
    
    # Final feedback based on score
    if score == 4:
        st.success("✅ Your password is **Strong**! 🎉")
    elif score == 3:
        st.warning("✅ Your password is **Medium**. It could be stronger. 💡")
    else:
        st.error("❌ Your password is **Weak**! Consider improving it. ⚠️")
    
    # Display improvement tips if any
    if feedback:
        st.markdown("### Improvements Needed:")
        for tip in feedback:
            st.write(tip)
else:
    st.info(" Please  enter a password to get started.")
