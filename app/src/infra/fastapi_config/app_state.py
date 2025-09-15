from enum import Enum
from fastapi import FastAPI
from typing import Any

class AppStates(str, Enum):
    
    EXTERNAL_FASTAPI_PORT = "external_fastapi_port"
    INTERNAL_FASTAPI_PORT = "internal_fastapi_port"

def set_app_state(
    app: FastAPI,
    key: str,
    value: Any,
):
    """Set a state in the FastAPI app."""
    setattr(app.state, key, value)


def get_app_state(
    app: FastAPI,
    key: str,
):
    """Get a state from the FastAPI app."""
    return getattr(app.state, key)