"""server script.

Returns:
        _type_: _description_
"""
import aiohttp
from fastapi import FastAPI
import requests
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    """Test.

    Returns:
        dict: test response
    """
    return {"Message": "Server works"}

@app.get("/version")
def get_version():
    """Get the version of api.

    Returns:
        dict: the version of api
    """
    return {"Version": "1.0.0"}

@app.get("/q/{message}/{classes}")
async def response(message: str, classes: str = "AL"):
    """Elabare the command and send the result.

    Args:
        message (str): the command
        classes (str, optional): The class of command. Defaults to AL.

    Returns:
        _type_: _description_
    """
    return {"message": message, "class": classes}


# --- FUNCTION TESTING ---
# Endpoint Sincrono
@app.get("/synchronous")
def synchronous_endpoint():
    """Test di funziona synchronous.

    Returns:
        dict: message standard
    """
    response = requests.get("https://httpbin.org/delay/2")  # Simula una chiamata HTTP che impiega 2 secondi
    return {"message": "Synchronous endpoint!", "status": response.status_code}

# Endpoint Asincrono
@app.get("/asynchronous")
async def asynchronous_endpoint():
    """Test di funziona asynchronous.

    Returns:
        dict: message standard
    """
    async with aiohttp.ClientSession() as session, session.get("https://httpbin.org/delay/2") as response:
        return {"message": "Asynchronous endpoint!", "status": response.status}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=1010)
