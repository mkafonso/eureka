from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackBot:
    def __init__(self, api_token):
        # Initialize SlackBot with the Slack API token.
        self.client = WebClient(token=api_token)

    def send_message(self, channel='#building-stuffs', message="Hello world!"):
        # Send a message to a Slack channel.
        try:
            response = self.client.chat_postMessage(channel=channel, text=message)
            # Check if the message text in the response matches the sent message.
            assert response["message"]["text"] == message
            print("Mensagem enviada com sucesso")
        except SlackApiError as e:
            print(f"Não consegui enviar a mensagem: {e.response['error']}")

    def run(self, channel='#building-stuffs', message="Hello world!"):
        # Execute the bot by sending a message to a Slack channel.
        self.send_message(channel=channel, message=message)
