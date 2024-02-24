from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/")
async def get_messages() -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=[
            {"id": 1, "message": "Hello, World!"},
            {"id": 2, "message": "Goodbye, World!"},
        ],
    )
