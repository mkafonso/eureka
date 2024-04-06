from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackBot:
    def __init__(self, api_token):
        # Inicializa o SlackBot com o token da API do Slack.
        self.client = WebClient(token=api_token)

    def send_message(self, channel='#building-stuffs', message="Hello world!"):
        #  Envia uma mensagem para um canal no Slack.
        try:
            response = self.client.chat_postMessage(channel=channel, text=message)
            assert response["message"]["text"] == message
            print("Mensagem enviada com sucesso")
        except SlackApiError as e:
            print(f"Não consegui enviar a mensagem: {e.response['error']}")

    def run(self, channel='#building-stuffs', message="Hello world!"):
        # Executa o bot enviando uma mensagem para um canal no Slack.
        self.send_message(channel=channel, message=message)
