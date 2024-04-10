import os
from dotenv import load_dotenv

# Load environment variables from a .env file in the project root.
def load_environment_variables():
    env_path = ".env"
    if os.path.exists(env_path):
        load_dotenv(env_path)
    else:
        print(".env file not found.")

# Get the value of an environment variable.
def get_environment_variable(key):
    return os.getenv(key)

# Get the value of an environment variable and raise an error if it's not defined.
def require_environment_variable(key):
    value = get_environment_variable(key)
    if value is None:
        raise KeyError(f"environment variable '{key}' is not defined.")
    return value
