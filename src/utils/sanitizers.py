# Remove bot mentions from a Slack message and strip leading/trailing spaces.
def sanitize_slack_message(message):
    # List of user mentions to remove from the message
    # Example: @Eureka || @Eureka,
    user_mentions = ['<@U06T63KKCH2>, ', '<@U06T63KKCH2>']

    # Remove each mention from the message
    for mention in user_mentions:
        message = message.replace(mention, '')

    # Strip leading and trailing spaces from the sanitized message
    sanitized_message = message.strip()

    return sanitized_message
