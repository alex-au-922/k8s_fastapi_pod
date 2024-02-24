from fastapi import APIRouter
from .messages import router as messages_router
from .healthcheck import router as healthcheck_router

router = APIRouter()

router.include_router(messages_router, prefix="/messages", tags=["messages"])
router.include_router(healthcheck_router, prefix="/healthcheck", tags=["healthcheck"])
