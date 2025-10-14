import streamlit as st
import google.generativeai as genai

# --- Set your Gemini API key ---
API_KEY = "AIzaSyDZWLZmaD-LiXzv7ZCcs0sBwcb-zWYi-QQ"  # Replace with your key

# --- Configure Gemini ---
genai.configure(api_key=API_KEY)

# --- Streamlit UI ---
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
        model = genai.GenerativeModel("gemini-2.0-flash")  # ✅ use GenerativeModel
        response = model.generate_content(prompt)

    travel_plan = response.text

    st.subheader("🗺️ Your AI Travel Plan:")
    st.write(travel_plan)

    # --- Download option ---
    file_name = f"Travel_Plan_{destination.replace(' ', '_')}.txt"
    st.download_button(
        label="💾 Download Travel Plan",
        data=travel_plan,
        file_name=file_name,
        mime="text/plain"
    )
