import requests

import logging
import lib.logger

def download_model_en():
    """Download model english."""
    url = "https://filemodelen.s3.eu-north-1.amazonaws.com/model_en.pkl"
    destination = 'models/model_en.pkl'
    try:
        response = requests.get(url, stream=True, timeout=None)
        with open(destination, 'wb') as file:
            file.write(response.content)
    except requests.exceptions.RequestException:
        logging.error("For some reason i not enable to download the english models sorry")
    except OSError:
        logging.error("For some reason i not enable to download the english models sorry")
