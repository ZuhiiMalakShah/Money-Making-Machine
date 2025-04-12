import streamlit as st  # Streamlit for UI
import random  # Random number generator
import time  # Time handling
import requests  # Web requests

# Set up page title and layout
st.set_page_config(page_title="Money Making Machine", page_icon="💰", layout="centered")
st.title("💰 Money Making Machine 💸")
st.markdown("Unlock your financial potential with fun and motivation!")

# Function to create a random amount of money
def generate_money():
    return random.randint(50, 5000)  # More realistic money range

# Create a section for generating money
st.subheader("🚀 Instant Cash Generator")
if st.button("💵 Generate Money"):
    with st.spinner("Counting your money..."):
        time.sleep(3)  # Reduced wait time
        amount = generate_money()
        st.success(f"🎉 You just made **${amount}**!")

# Function to fetch side hustle ideas
def fetch_side_hustle():
    try:
        response = requests.get("https://fastapi-api.vercel.app/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles.get("side_hustle", "Freelancing")
    except requests.RequestException:
        return "🚀 Start a YouTube channel!"
    return "📈 Invest in stocks!"

# Create a section for side hustle ideas
st.subheader("💡 Side Hustle Ideas")
if st.button("📊 Generate Hustle"):
    with st.spinner("Finding the best hustle for you..."):
        time.sleep(2)
        idea = fetch_side_hustle()
        st.success(f"🔥 Try this: **{idea}**")

# Function to fetch motivational quotes
def fetch_money_quote():
    try:
        response = requests.get("https://fastapi-api.vercel.app/money_quotes")
        if response.status_code == 200:
            quotes = response.json()
            return quotes.get("money_quote", "Time is money!")
    except requests.RequestException:
        return """💡 **"The best investment you can make is in yourself."** - Warren Buffett"""
    return "💰 ""A wise person should have money in their head, but not in their heart."""

# Create a section for money motivation
st.subheader("🌟 Money-Making Motivation")
if st.button("💬 Get Inspired"):
    with st.spinner("Fetching an inspiring quote..."):
        time.sleep(2)
        quote = fetch_money_quote()
        st.info(quote)

# Footer
st.markdown("---")
st.caption("🚀 Created with ❤️ by Zuhii Shah")
