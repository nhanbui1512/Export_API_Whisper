from fastapi import HTTPException, Header
from app.core.config import get_valid_api_keys

async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key not in get_valid_api_keys():
        raise HTTPException(status_code=401, detail="Unauthorized")
    return x_api_key
