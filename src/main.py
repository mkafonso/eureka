from utils.environment_variables import load_environment_variables
from utils.environment_variables import require_environment_variable
from integrations.slack import SlackBot

def main():
    # Carrega as variáveis de ambiente do arquivo .env
    load_environment_variables()

    # Pegar o token da API do Slack a partir das variáveis de ambiente
    slack_api_token = require_environment_variable("SLACK_API_TOKEN")

    # Criar instância do bot Slack
    bot = SlackBot(slack_api_token)
    bot.run()

if __name__ == "__main__":
    main()
