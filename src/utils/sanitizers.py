# Remove menções do bot de uma mensagem do Slack e remove os espaços iniciais/finais.
def sanitize_slack_message(message):
    # Exemplo: @Eureka || @Eureka,
    user_mentions = ['<@U06T63KKCH2>, ', '<@U06T63KKCH2>']

    for mention in user_mentions:
        message = message.replace(mention, '')

    sanitized_message = message.strip()

    return sanitized_message
