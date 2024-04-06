from queue import Queue

# Fila para armazenar eventos do Slack
slack_event_queue = Queue()

# Função para lidar com o evento de menção de aplicativo
def handle_app_mention(payload):
    slack_event_queue.put(payload)
