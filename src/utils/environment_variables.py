import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente a partir de um arquivo .env na raiz do projeto.
def load_environment_variables():
    env_path = ".env"
    if os.path.exists(env_path):
        load_dotenv(env_path)
    else:
        print("Arquivo .env não encontrado.")

# Obtém o valor de uma variável de ambiente.
def get_environment_variable(key):
    return os.getenv(key)

# Obtém o valor de uma variável de ambiente e retorna um erro se não estiver definida.
def require_environment_variable(key):
    value = get_environment_variable(key)
    if value is None:
        raise KeyError(f"A variável de ambiente '{key}' não está definida.")
    return value
