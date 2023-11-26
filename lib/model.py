"""File main for the use of models.

Returns:
    _type_: _description_
"""
import os
import logging
import sys

import joblib
from vectorizer import GloVeVectorizer,sentence_to_vec  # noqa: F401


class Model:
    """A class to load and use the trained model."""
    def __init__(self):
        """Initializes a new instance of the Model class."""
        self.base_path = os.getcwd()
        self.path_input = os.path.join(self.base_path, "data","in")
        self.path_output = os.path.join(self.base_path, "data","out")
        self.path_model = os.path.join(self.base_path, "models")
        model_it,model_en = self.load_models()
        self.avaible_language = ["it","en"]
        self.models = {
            "it": model_it,
            "en": model_en
        }

    def load_models(self):
        """Load the models from disk.

        Returns:
            _type_: _description_
        """
        logging.info("Loading the models")
        model_it = joblib.load(os.path.join(self.path_model,"model_it.pkl"))
        model_en = joblib.load(os.path.join(self.path_model,"model_en.pkl"))
        logging.info("Models loaded correctly")
        return model_it,model_en

    def make_prediction(self,message:str,lang:str = 'en') -> str:
        """Make prediction with the loaded models.

        Args:
            message (str): The message to predict the class
            lang (str): the language or the message

        Returns:
            str: _description_
        """
        for language in self.avaible_language:
            if language == lang:
                return self.models[lang].predict([message])[0]
        logging.error("The language is not supported")
        sys.exit()

    def write_output(self,class_predicted:str):
        """Write the predicted class into a file.

        Args:
            class_predicted (str): _description_
        """
        try:
            with open(self.path_output,"w",encoding="utf-8") as file:
                    file.write(class_predicted)
        except OSError as error:
            logging.error(f"An errore occured with output file: {error}")
            sys.exit()

    def run(self):
        """Run the application."""
        status = True
        try:
            while(status):
                try:
                    with open(self.path_input,encoding="utf-8") as file:
                        data = file.read()
                    logging.debug("Loading the data from input file")
                except OSError as error:
                    logging.error(f"An errore occured with input: {error}")
                    status = False
                    sys.exit(0)
                if not data:
                    logging.debug("No data in the file")
                    continue
                else:
                    logging.debug("Data loaded correctly and the file is not empty")
                    try:
                        message = data.split("|")[0]
                        lang = data.split("|")[1]
                    except IndexError as error:
                        logging.error(f"Error occured in the formatting text phase {error}")
                        sys.exit()
                    class_predicted = self.make_prediction(message=message,lang=lang)
                    logging.debug("Writing the file")
                    self.write_output(class_predicted=class_predicted)
        except KeyboardInterrupt:
            logging.info("Execution closed")



if __name__ == "__main__":
    model = Model()
    model.run()
