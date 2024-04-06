from utils.environment_variables import load_environment_variables
from utils.environment_variables import require_environment_variable
from server import create_app

def main():
    # Carrega as variáveis de ambiente do arquivo .env
    load_environment_variables()

    # Pegar o token da API do Slack a partir das variáveis de ambiente
    slack_api_token = require_environment_variable("SLACK_API_TOKEN")
    slack_signing_secret = require_environment_variable("SLACK_SIGNING_SECRET")
    server_port = require_environment_variable("SERVER_PORT")

    # Cria a instância da aplicação Flask com os tokens configurados
    app = create_app(slack_api_token, slack_signing_secret)
    app.run(debug=True, port=server_port)

if __name__ == "__main__":
    main()
