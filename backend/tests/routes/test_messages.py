from fastapi import status
import httpx

import pytest
from src.app import app


@pytest.mark.anyio
async def test_messages() -> None:
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/api/messages/")
        assert response.status_code == status.HTTP_200_OK
        response = response.json()
        assert isinstance(response, list)
        for message in response:
            assert isinstance(message, dict)
            assert "id" in message
            assert isinstance(message["id"], int)
            assert "message" in message
            assert isinstance(message["message"], str)
