import pandas as pd
import tensorflow as tf
import numpy as np

#%%
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(250, input_shape=(1,), activation="relu"),
    tf.keras.layers.Dense(100, activation=tf.keras.activations.relu),
])

#%%
model.compile(
    loss=tf.keras.losses.mse,
    optimizer=tf.keras.optimizers.Adam(),
    metrics=["mae"]
)