from utils.environment_variables import load_environment_variables
from utils.environment_variables import require_environment_variable
from server import create_app

def main():
    # Carrega as variáveis de ambiente do arquivo .env
    load_environment_variables()

    # Pegar o token da API do Slack a partir das variáveis de ambiente
    SLACK_API_TOKEN = require_environment_variable("SLACK_API_TOKEN")
    SLACK_SIGNING_SECRET = require_environment_variable("SLACK_SIGNING_SECRET")
    OPENAI_API_KEY = require_environment_variable("OPENAI_API_KEY")
    SERVER_PORT = require_environment_variable("SERVER_PORT")

    # Cria a instância da aplicação Flask com os tokens configurados
    app = create_app(SLACK_API_TOKEN, SLACK_SIGNING_SECRET, OPENAI_API_KEY)
    app.run(debug=True, port=SERVER_PORT)

if __name__ == "__main__":
    main()
