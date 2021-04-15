import tensorflow as tf

#%% Method1
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(3, input_shape=(2,)))
model.add(tf.keras.layers.Dense(1))
model.summary()

#%% Method2
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(3, input_shape=(2,)),
    tf.keras.layers.Dense(1)
])
#%%
model.summary()