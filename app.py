from flask import Flask, request
from slack_bolt.adapter.flask import SlackRequestHandler
from slack_bolt import App
import openai as client
import os
import time
import gunicorn
from dotenv import load_dotenv
from models import db, UserThread  # Import the database and model

# Load environment variables from a .env file (if you're using one)
load_dotenv()

# Use environment variables for security
slack_bot_token = os.getenv("SLACK_BOT_TOKEN")
slack_signing_secret = os.getenv("SLACK_SIGNING_SECRET")
openai_api_key = os.getenv("OPENAI_API_KEY")
assistant_id = os.getenv("OPENAI_ASSISTANT_ID")  # The ID of your Assistant
user_threads = {}
# Initializes your app with your bot token and signing secret
app = App(token=slack_bot_token, signing_secret=slack_signing_secret)

# Initializes OpenAI client
client.api_key = openai_api_key

flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'  # Configure your database URI
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(flask_app)

with flask_app.app_context():
    db.create_all()  # Create database tables
# Listen to all messages in direct messages
import time

# Assuming the rest of your setup code remains the same
handler = SlackRequestHandler(app)

def handle_message(message, say):
    user = message['user']
    user_query = message['text']
    
    # Query the database for the user's thread_id
    user_thread = UserThread.query.filter_by(user_id=user).first()
    
    if user_thread:
        thread_id = user_thread.thread_id
    else:
        # Create a new thread and store the thread_id
        thread = client.beta.threads.create(messages=[{"role": "user", "content": user_query}])
        thread_id = thread.id
        new_user_thread = UserThread(user_id=user, thread_id=thread_id)
        db.session.add(new_user_thread)
        db.session.commit()
    
    # Initiate a run to process the conversation with the assistant
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
        instructions="Você é um profissional de RH da Dattos e tem acesso aos arquivos para informar as pessoas sobre as duvidas acerca de políticas de rh.",  # Add your own instructions if needed
    )
    
    # Wait for the run to complete (simple polling mechanism)
    while True:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        if run_status.status == "completed":
            break
        time.sleep(1)  # Sleep for a short period before checking again
    
    # Retrieve messages added to the thread by the assistant
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    
    # Extract the latest assistant message to send as a reply in Slack
    if messages.data:
        assistant_messages = [msg for msg in messages.data if msg.role == "assistant"]
        if assistant_messages:
            ai_response = assistant_messages[-1].content[0].text.value

        else:
            ai_response = "Sorry, I couldn't find a response."
    else:
        ai_response = "Sorry, I couldn't process your request."

    # Use the AI's response to reply in Slack
    say(f"<@{user}>, {ai_response}")


flask_app = Flask(__name__)
handler = SlackRequestHandler(app)

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

if __name__ == "__main__":
    port = os.getenv("PORT", 3000)
    flask_app.run(port=int(port))
