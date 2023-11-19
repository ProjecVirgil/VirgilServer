import os
import logging
import string
import time

from fastapi import FastAPI





class Api:

    def __init__(self):
        self.app = FastAPI()
        self.base_path = os.getcwd()
        self.path_input = os.path.join(self.base_path, "data","in")
        self.path_output = os.path.join(self.base_path, "data","out")

        #Simple cleaning to allow the model to function better
        original_punctuation = string.punctuation
        exceptions = ":'"
        self.custom_punctuation = "".join([char for char in original_punctuation if char not in exceptions])

    def clean_input(self,message:str):
        """This method is used to clean the input message before it's processed by the NLP model. It removes all punctuations except ':''.

        Args:
            message (str): _description_

        Returns:
            _type_: _description_
        """
        # Convert text to lowercase
        message = message.lower()
        # Remove punctuation
        message = message.translate(str.maketrans(' ', ' ', self.custom_punctuation))
        # Remove stopwords and lemmatize the words
        words = message.split()
        return ' '.join(words)

api = Api()
app = api.app

@app.get("/")
def read_root():
    """Sanity check.

    Returns:
        dict: test response
    """
    return {"Message": "Server works"}

'''
        original_punctuation = string.punctuation
        exceptions = ":'"
        self.custom_punctuation = "".join([char for char in original_punctuation if char not in exceptions])


'''
@app.get("/q/{lang}/{message}")
def predictions(lang:str,message:str):
    """Sanity check.

    Returns:
        dict: test response
    """
    message = api.clean_input(message=message)
    with open(api.path_input,"w",encoding='utf-8') as file:
        file.write(f"{message}|{lang}")
    time.sleep(0.2)
    with open(api.path_output,encoding='utf-8') as file:
        classes_predicted = file.read()
        if not classes_predicted:
            raise Exception("No prediction found.")
        else:
            return {"Classes predicted":classes_predicted}
