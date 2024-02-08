import requests
import json
import os

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
    webhook_url = os.getenv("SLACK_CHANNEL_WEBHOOKURL")
    message = "TESTE"
    send_slack_message(webhook_url, message)
