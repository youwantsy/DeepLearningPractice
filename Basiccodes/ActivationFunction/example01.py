import tensorflow as tf
import numpy as np

train_x = np.random.normal(0, 1, (1000,1))

def sigmoid(x):
    y = 2*x + 1
    if y > 0: return 1
    else: return 0

train_y = np.array([sigmoid(item) for item in train_x])

print(train_x.shape)
print(train_x[:3])
print(train_y.shape)
print(train_y[:3])

#%%
model = tf.keras.models.Sequential()
# model.add(tf.keras.layers.Dense(1, input_shape=(1,),
#                                 activation="sigmoid"))
model.add(tf.keras.layers.Dense(1, input_shape=(1,),
                                activation=tf.keras.activations.sigmoid))
model.summary()

#%%
model.compile(
    optimizer=tf.keras.optimizers.RMSprop(),
    loss=tf.keras.losses.binary_crossentropy
)
#%%
model.fit(train_x, train_y, epochs=1000)

#%%
new_x = tf.constant(10.0, shape=(1, 1))
new_y = model.predict(new_x)
print("x:{}, y:{}".format(new_x, new_y))
