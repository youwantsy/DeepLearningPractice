import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print("train_images:", train_images.shape)
print("train_labels:", train_labels.shape)
print()
print("test_images:", test_images.shape)
print("test_labels:", test_labels.shape)

#%% 데이터 전처리
train_images = train_images / 255.0
test_images = test_images / 255.0

#%% 모델 정의
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

#%%
model.compile(
    optimizer=tf.keras.optimizers.RMSprop(),
    loss=tf.keras.losses.sparse_categorical_crossentropy,
    metrics=['accuracy']
)

#%%
model.fit(train_images, train_labels, epochs=5)

#%% 평가
model.evaluate(test_images,test_labels)

#%% 추론하기
index = np.random.randint(0, 10)
plt.imshow(test_images[index], cmap="gray")
plt.show()
input = tf.constant(test_images[index], shape=(1,28,28))
output = model.predict(input)
number = np.argmax(output)
print("숫자 {} 입니다.".format(number))