from fastapi import status
import httpx

import pytest
from src.app import app


@pytest.mark.anyio
async def test_healthcheck() -> None:
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/api/healthcheck/")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"message": "ok"}
