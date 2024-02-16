from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.api.common import create_db
from app.api.router import api_router
from app.settings import settings

app: FastAPI = FastAPI(
    title="Task Manager",
    description="Manages tasks to be worked on",
    openapi_url=f"{settings.api_path_str}/openapi.json",
)

settings.check()
create_db()
app.include_router(api_router, prefix=settings.api_path_str)


@app.get(
    "/",
    response_class=RedirectResponse,
    description="Redirects the user to the API docs",
    summary="Redirect to API docs",
    tags=["Index"],
)
async def home() -> str:
    """Redirect requests to host to docs endpoint.
    :return: the redirected URL
    """
    return f"{settings.host_url}/docs"
