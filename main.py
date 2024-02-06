from flask import Flask, request
from slack_bolt.adapter.flask import SlackRequestHandler
from slack_bolt import App
import openai
import os
from dotenv import load_dotenv

# Load environment variables from a .env file (if you're using one)
load_dotenv()

# Use environment variables for security
slack_bot_token = os.getenv("SLACK_BOT_TOKEN")
slack_signing_secret = os.getenv("SLACK_SIGNING_SECRET")
openai_api_key = os.getenv("OPENAI_API_KEY")
assistant_id = os.getenv("OPENAI_ASSISTANT_ID")  # The ID of your Assistant

# Initializes your app with your bot token and signing secret
app = App(token=slack_bot_token, signing_secret=slack_signing_secret)

# Initializes OpenAI client
openai.api_key = openai_api_key

# Listen to all messages in direct messages
@app.message()
def handle_message(message, say):
    user = message['user']
    user_query = message['text']
    
    # Sends the message to the OpenAI Assistants API
    response = openai.beta.threads.runs.create(
        assistant_id=assistant_id,
        model="gpt-3.5-turbo",  # Specify the model your Assistant uses
        messages=[{"role": "user", "content": user_query}]
    )
    
    # Use the response from the Assistants API to reply in Slack
    say(f"<@{user}>, {response.choices[0].message.content}")

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

if __name__ == "__main__":
    port = os.getenv("PORT", 3000)
    flask_app.run(port=int(port))
