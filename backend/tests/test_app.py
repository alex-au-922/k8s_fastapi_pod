from fastapi import status
import httpx

import pytest
from src.app import app
from .conftest import random_paths


@pytest.mark.anyio
@pytest.mark.parametrize("path", [f"/{path}" for path in random_paths()])
async def test_root_route_404(path: str) -> None:
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get(path)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == {"message": "Not Found"}
