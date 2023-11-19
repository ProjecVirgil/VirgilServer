import os
import subprocess
import sys

from colorama import Fore,Style
import logging
import requests

import lib.logger

BANNER = Style.BRIGHT + Fore.MAGENTA + '''
  ________ _______ ___________ ____  ____   _______
 /"       )"     "("     _   "|"  _||_ " | |   __ "\    
(:   \___(: ______))__/  \\__/|   (  ) : | (. |__) :)       
 \___  \  \/    |     \\_ /   (:  |  | . ) |:  ____/       
  __/  \\ // ___)_    |.  |    \\ \__/ //  (|  /        
 /" \   :|:      "|   \:  |    /\\ __ //\ /|__/ \       
(_______/ \_______)    \__|   (__________|_______)        

'''


class Main():

    def __init__(self):
        self.base_path = os.getcwd()
        self.pid = os.getpid()
        self.PORT = 8080
        self.IP = "127.0.0.1"

    def init(self):
        """Initialize the main class and set up logger."""
        print(BANNER,flush=True)
        logging.info(f"PID [{self.pid}]")
        logging.info("Init setup")
        path_model_en = os.path.join(self.base_path, "models","model_en.pkl")
        if not os.path.exists(path_model_en):
            self.download_model_en(path_model_en)
        logging.info("English models alredy installed")
        logging.info("Creating file input/output")
        try:
            self.init_in_out()
        except Exception as error:
            logging.error(f"An error occurred: {error}")
            sys.exit(1)
        logging.info("File created succefully")

    def download_model_en(self,destination):
        """Download model english."""
        logging.info("Downloding english model")
        url = "https://filemodelen.s3.eu-north-1.amazonaws.com/model_en.pkl"
        try:
            response = requests.get(url, stream=True, timeout=None)
            with open(destination, 'wb') as file:
                file.write(response.content)
        except requests.exceptions.RequestException as error:
            logging.error(f"For some reason i not enable to download the english models sorry: {error}")
            sys.exit(1)
        except OSError as error:
            logging.error(f"For some reason i not enable to download the english models sorry: {error}")
            sys.exit(1)

    def init_in_out(self):
        """Create a folder with file for save and load data."""
        path_in = os.path.join(self.base_path, "data","in")
        path_out = os.path.join(self.base_path, "data","out")
        with open(path_in,encoding="utf-8",mode="w") as file:
            file.write("")
        with open(path_out,encoding="utf-8",mode="w") as file:
            file.write("")

    def run(self):
        """Run the program."""
        uvicorn_process = subprocess.Popen(['uvicorn', 'lib.api:app', '--host' , self.IP , '--port', self.PORT])
        model_process = subprocess.Popen([sys.executable, 'lib/model.py'])
        logging.info(f"Uvicorn PID: {uvicorn_process.pid}")
        logging.info(f"Model PID: {model_process.pid}")

if __name__ == "__main__":
    main = Main()
    main.init()
    main.run()
