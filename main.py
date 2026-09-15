from tensorflow import *
from keras.utils import to_categorical
from flask import Flask, request, jsonify, render_template
import keras

import pandas as pd

from src.app import *

app = Flask(__name__)

#Ejecución Principal
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
