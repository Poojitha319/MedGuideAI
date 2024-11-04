import chainlit as cl
from chatbot import Chatbot

# Create an instance of the chatbot
chatbot = Chatbot()

# Chainlit interface
@cl.on_chat_message
def main(user_input):
    if "get location" in user_input.lower():
        cl.message("Fetching your location...")
        cl.js("""
        navigator.geolocation.getCurrentPosition(function(position) {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            chainlit.send({ lat, lon });
        }, function() {
            chainlit.send({ error: "Unable to retrieve your location." });
        });
        """)
    else:
        response = chatbot.handle_input(user_input)
        cl.message(response)

@cl.on_message
def handle_location(data):
    if "lat" in data and "lon" in data:
        user_location = f"{data.lat},{data.lon}"  # Combine latitude and longitude
        chatbot.set_user_location(user_location)
        cl.message(f"Location set to: {user_location}")
    elif "error" in data:
        cl.message(data.error)

if __name__ == "__main__":
    cl.run()
