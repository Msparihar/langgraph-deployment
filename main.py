import requests
from typing import Optional

BASE_API_URL = "http://127.0.0.1:7860"


def run_flow(
    message: str,
    endpoint: str,
    session_id: Optional[str] = None,
    output_type: str = "chat",
    input_type: str = "chat",
    tweaks: Optional[dict] = None,
    api_key: Optional[str] = None,
) -> dict:
    """
    Run a flow with a given message and optional tweaks.

    :param message: The message to send to the flow
    :param endpoint: The ID or the endpoint name of the flow
    :param session_id: Optional session ID to maintain conversation context
    :param output_type: Type of output expected from the flow
    :param input_type: Type of input being sent to the flow
    :param tweaks: Optional tweaks to customize the flow
    :param api_key: Optional API key for authentication
    :return: The JSON response from the flow
    """
    api_url = f"{BASE_API_URL}/api/v1/run/{endpoint}"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }

    if session_id:
        payload["session_id"] = session_id
    if tweaks:
        payload["tweaks"] = tweaks

    headers = None
    if api_key:
        headers = {"x-api-key": api_key}

    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()


# Example usage
if __name__ == "__main__":
    flow_id = "d8b91240-e65c-4aa0-95bd-f043541aabf9"
    message = "Hello, how are you?"
    session_id = "user-123"  # Optional session ID
    response = run_flow(message=message, endpoint=flow_id, session_id=session_id)
    print(response)
