from flask import Flask, request
from slackeventsapi import SlackEventAdapter
from integrations.slack import SlackBot
from integrations.langchain import initialize_langchain_model, process_langchain_query
from utils.events import handle_app_mention, slack_event_queue
from utils.sanitizers import sanitize_slack_message
import threading

# Function to create Flask server and Slack Bot
def create_app(slack_api_token, slack_signing_secret, openai_api_key):
    app = Flask(__name__)

    # Instantiate the SlackBot with Slack API token
    slack_bot = SlackBot(slack_api_token)

    # Configure Slack event adapter to handle POST events at '/slack/events'
    slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events", app)

    # Initialize language chain model
    chain = initialize_langchain_model(openai_api_key, './data.txt')

    # Define route to handle Slack events
    @slack_events_adapter.on("app_mention")
    def handle_message(payload):
        handle_app_mention(payload)

    # Function to asynchronously process Slack events
    def process_slack_events():
        while True:
            # Get the next event from the queue (blocking)
            payload = slack_event_queue.get()
            event = payload.get('event', {})
            channel_id = event.get('channel')
            question = sanitize_slack_message(event.get('text'))

            # Process the question using the language chain model
            response = process_langchain_query(chain, question, [])

            # Use the SlackBot to send the processed message back to the channel
            slack_bot.run(channel=channel_id, message=response)

            # Mark the event as completed in the queue
            slack_event_queue.task_done()

    # Start asynchronous processing of Slack events in a separate thread
    processing_thread = threading.Thread(target=process_slack_events)
    processing_thread.start()

    return app
