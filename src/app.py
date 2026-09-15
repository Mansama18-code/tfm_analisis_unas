import tensorflow as tf
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from src.clasificacion import predecir

app = FastAPI(title="API de Clasificación de Alteraciones Ungueales")
# Permitir conexiones desde cualquier Frontend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_PATH = "/Users/mansama18/Desktop/webdiseno/unir/TFM/v2/models/mejor_modelo_EfficientNetB0.h5"
modelo = tf.keras.models.load_model(MODEL_PATH)

#APP de Clasificación Ungueal
@app.post("/predict")
async def predict(file: UploadFile = File(...), model = modelo):
    image_bytes = await file.read()
    predeccion = await predecir(image_bytes, model)
    return predeccion

