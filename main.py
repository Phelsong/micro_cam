""" App Framework """
# libs
import os
from typing import Annotated

import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse


# ----------------
app = FastAPI()
# ^ must be before local imports
# ----------------
# imports
from services.compute_service import map_to_gcode

# -----------------------------------------------------------------------------
origins = ["http://localhost", "http://127.0.0.1"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------------------------------------------


@app.get("/health")
def health() -> dict[str, str]:
    return {"You've Got": "Py"}


# -----------------------------------------------------------------------------


# TODO: ROUTE FOR PREVIOUS IMPLEMENTATION >> LEFT ONLY FOR REFERENCE/REMINDER
@app.post("/upload_file/", response_class=HTMLResponse)
async def create_upload_file(
    files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ],
):
    """Endpoint for Multi file upload"""
    for file in files:
        with open(f".\\uploads\\{file.filename}", "wb") as f:
            f.write(file.file.read())
        print(f"File uploaded: {file.filename}")
        map_to_gcode(f"uploads\\{file.filename}")


# -----------------------------------------------------------------------------

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         await websocket.send_text(f"Message text was: {data}")


# -------------------------------------------------------------------------------

# security = HTTPBasic()

# @app.get("/users/me")
# def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
#     return {"username": credentials.username, "password": credentials.password}


# -----------------------------------------------------------------------------


# ============================================================================
# Server configuration
config = uvicorn.Config(
    "main:app",
    host="::" if os.getenv("ENVIRONMENT") == "dev" else "0.0.0.0",
    port=(8011) if os.getenv("ENVIRONMENT") == "dev" else (8004),
    reload=True if os.getenv("ENVIRONMENT") == "dev" else False,
)
server = uvicorn.Server(config)
if __name__ == "__main__":
    server.run()
