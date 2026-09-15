import numpy as np
from preproceso.preprocess import preprocess_image

# Cargar el modelo guardado por el script de Jupyter


CLASS_NAMES = ['beau_s line', 'black line', 'clubbing', 'normal', 'onicomicosis', 'white spot']

def predecir(image_bytes, model):

    tensor_image = preprocess_image(image_bytes)
    # Realizar inferencia
    predictions = model.predict(tensor_image)[0]
    best_idx = int(np.argmax(predictions))
    confidence = float(predictions[best_idx])
    
    # Desglose de probabilidades por clase
    coincidencias_visuales = {
        CLASS_NAMES[i]: round(float(predictions[i]), 4)
        for i in range(len(CLASS_NAMES))
    }
    
    # Respuesta en formato JSON con lenguaje orientativo no diagnóstico
    return {
        "estado": "Exitoso",
        "patron_predominante": CLASS_NAMES[best_idx],
        "indice_confianza": round(confidence, 4),
        "coincidencias_visuales": coincidencias_visuales,
        "advertencia_legal": "Resultado orientativo basado en similitud visual. No constituye diagnóstico médico."
    }
