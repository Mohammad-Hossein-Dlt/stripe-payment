from app.src.infra.fastapi_config.app import app
from app.src.infra.fastapi_config.app_state import AppStates, get_app_state

def get_app_ports_depend() -> tuple[int, int]:
    
    external_port = get_app_state(app, AppStates.EXTERNAL_FASTAPI_PORT)
    internal_port = get_app_state(app, AppStates.INTERNAL_FASTAPI_PORT)
    
    return external_port, internal_port