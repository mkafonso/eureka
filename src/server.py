from flask import Flask, request
from slackeventsapi import SlackEventAdapter
from integrations.slack import SlackBot
from utils.events import handle_app_mention, slack_event_queue
import threading

# Função para configurar o servidor Flask e o Slack Bot
def create_app(slack_api_token, slack_signing_secret):
    app = Flask(__name__)

    # Instancia o SlackBot com o token da API do Slack
    slack_bot = SlackBot(slack_api_token)

    # Configura o adaptador de eventos do Slack para lidar com eventos POST em '/slack/events'
    slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events", app)

    # Define a rota para lidar com eventos do Slack
    @slack_events_adapter.on("app_mention")
    def handle_message(payload):
        handle_app_mention(payload)

    # Função para processar assincronamente os eventos do Slack
    def process_slack_events():
        while True:
            # Obtem o próximo evento da fila (bloqueante)
            payload = slack_event_queue.get()
            event = payload.get('event', {})
            channel_id = event.get('channel')
            question = event.get('text')

            # Processa a mensagem usando o SlackBot
            slack_bot.run(channel=channel_id, message=question)

            # Marca o evento como concluído na fila
            slack_event_queue.task_done()

    # Inicia o processamento assíncrono dos eventos do Slack em uma thread separada
    processing_thread = threading.Thread(target=process_slack_events)
    processing_thread.start()

    return app
