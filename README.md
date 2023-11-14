# Proyecto de Predicción de Números de Lotería

## Descripción del Proyecto
Este repositorio contiene implementaciones de modelos de predicción de números de lotería utilizando técnicas de aprendizaje profundo. Se exploran dos enfoques principales: un modelo de regresión lineal y un modelo basado en redes neuronales LSTM (Long Short-Term Memory).

## Modelo de Regresión Lineal
En el script `linear_prediction.py`, se presenta un modelo de regresión lineal que utiliza datos históricos de números de lotería para predecir los próximos siete números. La predicción se realiza utilizando la biblioteca scikit-learn.

## Modelo LSTM para Predicción de Números
En los scripts `lstm_prediction.py` y `lstm_prediction_dropout.py`, se implementan modelos LSTM utilizando la biblioteca Keras. Estos modelos aprenden patrones en secuencias de números históricos y predicen los próximos números de la lotería. El segundo script incorpora capas de dropout y early stopping para mejorar la generalización del modelo y evitar sobreajustes.

## Guardar y Cargar Modelos
El script `save_load_model.py` muestra cómo guardar y cargar modelos entrenados para su uso futuro. Esto es útil para evitar la necesidad de volver a entrenar el modelo cada vez que se desea realizar una predicción.

## Entrenamiento con Nuevos Datos
El script `train_with_new_data.py` ilustra cómo entrenar los modelos con nuevos datos. Se asume que los nuevos datos están en un archivo CSV similar al utilizado para el entrenamiento original.

## Modelo con Predicción de un Único Número
En `single_number_prediction.py`, se presenta un modelo LSTM que predice un solo número de lotería, aplicando técnicas de dropout y early stopping.

## Estructura de Archivos
- `linear_prediction.py`: Modelo de regresión lineal.
- `lstm_prediction.py`: Modelo LSTM básico.
- `lstm_prediction_dropout.py`: Modelo LSTM con dropout y early stopping.
- `save_load_model.py`: Guardar y cargar modelos.
- `train_with_new_data.py`: Entrenar modelos con nuevos datos.
- `single_number_prediction.py`: Modelo LSTM para predecir un solo número.

## Requisitos
- NumPy
- Pandas
- scikit-learn
- Keras

## Instrucciones de Uso
1. Clona este repositorio: `git clone https://github.com/tu-usuario/nombre-del-repo.git`
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta los scripts según tus necesidades.

¡Explora, experimenta y diviértete prediciendo números de lotería con aprendizaje profundo!
