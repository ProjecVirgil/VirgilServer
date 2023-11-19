
import subprocess
import joblib

"""File for vectorize the sencente for the english model."""


'''model_filename_it = "models/model_it.pkl"
model_it = joblib.load(model_filename_it)

model_filename_en = "models/model_en.pkl"
model_en = joblib.load(model_filename_en)

pre = model_it.predict(["Che tempo fa"])
print(pre)
pre = model_en.predict(["What is the weather"])
print(pre)'''


process = subprocess.Popen(['uvicorn', 'api:app', '--port', '8000'])
process = subprocess.Popen(['python', 'model.py'])

print("SCRIPT AVVIATI")
