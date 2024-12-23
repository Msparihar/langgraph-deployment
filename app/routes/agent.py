from fastapi import APIRouter, HTTPException
from typing import Optional
import httpx
import uuid
import os

router = APIRouter(tags=["agent"])


@router.post("/chat_agent")
async def run_flow(user_query: str, session_id: Optional[str] = None):
    base_url = "http://127.0.0.1:7860"
    base_url = os.getenv("FLOW_SERVICE_URL", "http://host.docker.internal:7860")
    flow_id = "2dc53cb7-aef5-44a3-9d92-34140f95e713"

    headers = {"Content-Type": "application/json"}

    if not session_id:
        session_id = str(uuid.uuid4())

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{base_url}/api/v1/run/{flow_id}",
                headers=headers,
                params={"stream": "false"},
                json={
                    "input_value": user_query,
                    "output_type": "chat",
                    "input_type": "chat",
                    "session_id": session_id,
                    "tweaks": {
                        "Agent-tgf6r": {},
                        "ChatInput-K9lZX": {},
                        "ChatOutput-9fjJm": {},
                        "URL-DV3D9": {},
                        "CalculatorTool-vAx3J": {},
                    },
                },
            )

            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail="Flow execution failed")

            return response.json()

    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error communicating with flow service: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
