from utils.environment_variables import load_environment_variables
from utils.environment_variables import require_environment_variable
from server import create_app

def main():
    # Load environment variables from the .env file
    load_environment_variables()

    # Retrieve Slack API token from environment variables
    SLACK_API_TOKEN = require_environment_variable("SLACK_API_TOKEN")
    SLACK_SIGNING_SECRET = require_environment_variable("SLACK_SIGNING_SECRET")
    OPENAI_API_KEY = require_environment_variable("OPENAI_API_KEY")
    SERVER_PORT = require_environment_variable("SERVER_PORT")

    # Create a Flask application instance with configured tokens
    app = create_app(SLACK_API_TOKEN, SLACK_SIGNING_SECRET, OPENAI_API_KEY)

    # Run the Flask application
    app.run(debug=True, port=SERVER_PORT)

if __name__ == "__main__":
    main()
