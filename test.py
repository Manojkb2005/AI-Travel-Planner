import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=API_KEY)
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>

/* Animated Background */
.stApp {
    background: linear-gradient(-45deg,
        #0f172a,
        #111827,
        #1e3a8a,
        #0f766e);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    color: white;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Floating Glow Circles */
.glow {
    position: fixed;
    width: 300px;
    height: 300px;
    background: rgba(59,130,246,0.15);
    border-radius: 50%;
    filter: blur(80px);
    z-index: -1;
    animation: float 8s ease-in-out infinite;
}

.glow2 {
    top: 60%;
    left: 70%;
    background: rgba(6,182,212,0.15);
    animation-delay: 2s;
}

@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-30px);}
    100% {transform: translateY(0px);}
}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 70px;
    font-weight: 800;
    background: linear-gradient(
        90deg,
        #38bdf8,
        #818cf8,
        #06b6d4
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-top: 20px;
    animation: fadeIn 2s ease;
}

/* Subtitle */
.sub-title {
    text-align: center;
    font-size: 22px;
    color: #d1d5db;
    margin-bottom: 40px;
    animation: fadeIn 3s ease;
}

/* Glass Card */
.card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.1);
    backdrop-filter: blur(14px);
    padding: 30px;
    border-radius: 25px;
    box-shadow: 0px 8px 32px rgba(0,0,0,0.35);
    transition: 0.4s;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 12px 35px rgba(56,189,248,0.25);
}

/* Inputs */
.stTextInput input,
.stNumberInput input {
    border-radius: 12px !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    background-color: rgba(255,255,255,0.06) !important;
    color: white !important;
}

/* Button */
.stButton>button {
    width: 100%;
    height: 60px;
    border-radius: 15px;
    border: none;
    background: linear-gradient(
        90deg,
        #06b6d4,
        #3b82f6,
        #8b5cf6
    );
    color: white;
    font-size: 20px;
    font-weight: bold;
    transition: all 0.4s ease;
    box-shadow: 0px 0px 20px rgba(59,130,246,0.4);
}

.stButton>button:hover {
    transform: scale(1.03);
    box-shadow: 0px 0px 35px rgba(59,130,246,0.7);
}

/* Output Box */
.output-box {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.1);
    backdrop-filter: blur(12px);
    padding: 35px;
    border-radius: 25px;
    color: #f9fafb;
    font-size: 18px;
    line-height: 1.9;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.35);
    animation: fadeIn 1.5s ease;
}

/* Sidebar */
.css-1d391kg {
    background-color: rgba(15,23,42,0.9);
}

/* Fade Animation */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }

    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 50px;
    color: #9ca3af;
    font-size: 15px;
}

</style>

<div class="glow"></div>
<div class="glow glow2"></div>

""", unsafe_allow_html=True)



with st.sidebar:

    st.header("🌎 Travel Tips")

    st.markdown("""
    ✈️ Book flights early for cheaper prices  

    🍜 Try local street food safely  

    🏨 Stay near city centers  

    📸 Keep digital copies of documents  

    💳 Carry an international card  

    🌦️ Check weather before traveling
    """)

    st.markdown("---")

    st.subheader("🔥 Popular Destinations")

    st.markdown("""
    🇯🇵 Tokyo  
    🇫🇷 Paris  
    🇮🇹 Rome  
    🇰🇷 Seoul  
    🇦🇪 Dubai  
    🇹🇭 Bangkok
    """)

st.markdown(
    "<div class='main-title'>🌍 AI Travel Planner ✈️</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Experience next-generation AI powered vacation planning</div>",
    unsafe_allow_html=True
)

col1, col2 = st.columns([1.1, 1])
with col1:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    departure = st.text_input(
        "🛫 Departure",
        "Bangalore, India"
    )

    destination = st.text_input(
        "📍 Destination",
        "Tokyo, Japan"
    )

    days = st.number_input(
        "📅 Number of Days",
        min_value=1,
        value=5
    )

    interests = st.text_input(
        "🎯 Interests",
        "food, Culture, adventure"
    )

    generate = st.button("✨ Generate Smart Itinerary")

    st.markdown("</div>", unsafe_allow_html=True)

with col2:

    st.image(
        "https://images.unsplash.com/photo-1488646953014-85cb44e25828",
         width="stretch"
    )

if generate:

    prompt = f"""
    Create a luxury and detailed {days}-day travel itinerary.

    Departure: {departure}
    Destination: {destination}

    User interests:
    {interests}

    Include:
    - Morning activities
    - Afternoon activities
    - Evening activities
    - Famous attractions
    - Food recommendations
    - Local travel tips
    - Estimated daily budget
    - Hidden gems

    Format beautifully using bullet points.
    """

    try:

        with st.spinner(
            "🌏 AI is crafting your dream journey..."
        ):

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            travel_plan = (
                response.choices[0]
                .message.content
            )

        st.markdown(
            "## 🗺️ Your Personalized AI Itinerary"
        )

        st.markdown(
            f"<div class='output-box'>{travel_plan}</div>",
            unsafe_allow_html=True
        )

        # Download Button
        file_name = (
            f"Travel_Plan_"
            f"{destination.replace(' ', '_')}.txt"
        )

        st.download_button(
            label="💾 Download Travel Plan",
            data=travel_plan,
            file_name=file_name,
            mime="text/plain"
        )

    except Exception as e:

        st.error(f"Error: {str(e)}")

st.markdown(
    "<div class='footer'>Built with ❤️ using Streamlit + Groq AI</div>",
    unsafe_allow_html=True
)