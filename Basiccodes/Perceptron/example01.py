import tensorflow as tf
import numpy as np

train_x = np.random.normal(0, 1, (100,1))
train_y = 2*train_x + 1

print(train_x.shape, train_y.shape)

#%% 모델 정의
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(1, input_shape=(1,)))

model.summary()

#%% 모델 컴파일
model.compile(
    optimizer=tf.keras.optimizers.RMSprop(0.001),
    loss=tf.keras.losses.MeanSquaredError()
)
#%% 모델 학습
history = model.fit(train_x, train_y, epochs=1000)

#%% weight bias GET
w = model.get_weights()[0]
b = model.get_weights()[1]
print("w = ", w)
print("b = ", b)

#%% predict
new_x = tf.constant(10.0, shape=(1,1))
# new_x = np.array([[10.0]])

new_y = model.predict(new_x)
print("x:{}, y:{}".format(new_x, new_y))

#%%
import matplotlib.pyplot as plt
plt.plot(history.epoch, history.history["loss"], "r")
plt.title("Epoch Loss", fontsize="15")
plt.xlabel("Epoch", fontsize="13")
plt.ylabel("Loss", fontsize="13")
plt.xticks(fontsize="12")
plt.yticks(fontsize="12")
plt.show()

#%% 검증 및 평가
val_x = np.random.normal(0, 1, (20,1))
val_y = 2*val_x + 1
print(val_x.shape, val_y.shape)

test_x = np.random.normal(0, 1, (10,1))
test_y = 2 * test_x + 1
print(test_x.shape, test_y.shape)

history = model.fit(
    train_x, train_y,
    validation_data=(val_x,val_y),
    epochs=1000,
    batch_size=32
)

#%%
plt.title("loss")
plt.plot(history.epoch, history.history["loss"])
plt.show()

#%%
plt.title("val_loss")
plt.plot(history.epoch, history.history["val_loss"])
plt.show()

#%% 모델 테스트하기
test_loss = model.evaluate(test_x, test_y)
print(test_loss)

#%% 추론하기
new_x = np.array([[10.]])
new_y = model.predict(new_x)
print("x:{}, y:{}".format(new_x, new_y))