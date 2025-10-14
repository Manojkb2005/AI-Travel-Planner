import streamlit as st
import subprocess
import sys

# --- ✅ Auto-install google-generativeai if missing ---
try:
    import google.generativeai as genai
except ModuleNotFoundError:
    with st.spinner("📦 Installing dependencies... please wait..."):
        subprocess.check_call([sys.executable, "-m", "pip", "install", "google-generativeai==0.8.3"])
    import google.generativeai as genai

# --- 🔑 Your Gemini API Key (paste here) ---
API_KEY = "AIzaSyDZWLZmaD-LiXzv7ZCcs0sBwcb-zWYi-QQ"  # <-- Replace this with your actual API key

if not API_KEY or API_KEY.strip() == "":
    st.error("⚠️ Please enter your Gemini API key in the code!")
    st.stop()

# --- ✅ Configure Gemini ---
genai.configure(api_key=API_KEY)

# --- 🌍 Streamlit UI ---
st.title("🌍 AI Travel Planner ✈️")

departure = st.text_input("Enter departure:", "India, Bangalore")
destination = st.text_input("Enter destination:", "Tokyo, Japan")
days = st.number_input("Number of days:", min_value=1, value=3)
interests = st.text_input("Your interests:", "food, culture, adventure")

if st.button("Generate Plan"):
    prompt = (
        f"Plan a trip from {departure} to {destination}. "
        f"Create a {days}-day itinerary focusing on {interests}. "
        "Give a detailed, day-by-day plan in bullet points."
    )

    with st.spinner("✨ Generating your travel plan..."):
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)

    travel_plan = response.text

    st.subheader("🗺️ Your AI Travel Plan:")
    st.write(travel_plan)

    # --- 💾 Download button ---
    file_name = f"Travel_Plan_{destination.replace(' ', '_')}.txt"
    st.download_button(
        label="💾 Download Travel Plan",
        data=travel_plan,
        file_name=file_name,
        mime="text/plain"
    )

# --- Footer ---
st.markdown("---")
st.caption("✨ Powered by Google Gemini & Streamlit | Created by Manoj ✨")
