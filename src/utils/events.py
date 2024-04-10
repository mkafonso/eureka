from queue import Queue

# Queue to store Slack events
slack_event_queue = Queue()

# Function to handle the app mention event
def handle_app_mention(payload):
    # Put the incoming Slack event payload into the event queue
    slack_event_queue.put(payload)
