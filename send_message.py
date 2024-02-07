import requests
import json

def send_slack_message(webhook_url, message):
    """
    Sends a message to a Slack channel using a webhook URL.

    Parameters:
    - webhook_url (str): The Slack webhook URL.
    - message (str): The message to send.

    Returns:
    - response: The response object from the requests.post call.
    """
    # Prepare the payload
    payload = {'text': message}

    # Make the POST request to the Slack webhook
    response = requests.post(
        webhook_url,
        data=json.dumps(payload),
        headers={'Content-Type': 'application/json'}
    )

    # Check for success
    if response.status_code != 200:
        raise ValueError(
            f"Request to slack returned an error {response.status_code}, the response is:\n{response.text}"
        )

    return response

# Example usage
if __name__ == "__main__":
    webhook_url = "https://hooks.slack.com/services/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"
    message = "Olá, sou o bot da Dattos. Venha falar comigo. Clique no meu nome e me mande uma mensagem no privado!"
    send_slack_message(webhook_url, message)
