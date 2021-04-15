import tensorflow as tf
import matplotlib.pyplot as plt
#%%
dataset_path = "C:/JSY/datasets/mnist/mnist_png.tar/mnist_png"
train_path = dataset_path + "/training"
test_path = dataset_path + "/testing"

#%%
train_idg = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255.,
    validation_split=0.2
)

test_idg = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255.
)

train_dir_iterator = train_idg.flow_from_directory(
    train_path,
    target_size=(28,28),
    batch_size=32,
    color_mode="grayscale",
    class_mode="categorical",
    subset="training"
)

val_dir_iterator = train_idg.flow_from_directory(
    train_path,
    target_size = (28,28),
    batch_size=32,
    color_mode="grayscale",
    class_mode="categorical",
    subset="validation"
)

test_dir_iterator = test_idg.flow_from_directory(
    test_path,
    target_size=(28, 28),
    batch_size=32,
    color_mode="grayscale",
    class_mode="categorical"
)

#%%
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), input_shape=(28,28,1), activation="relu"),
    tf.keras.layers.MaxPool2D((2,2)),
    tf.keras.layers.Conv2D(64, (3,3),activation="relu"),
    tf.keras.layers.MaxPool2D((2,2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax")
])
model.summary()
#%%
model.compile(
    loss=tf.keras.losses.categorical_crossentropy,
    optimizer=tf.keras.optimizers.RMSprop(),
    metrics=["accuracy"]
)

#%%
history = model.fit_generator(
    train_dir_iterator,
    validation_data=val_dir_iterator,
    epochs=10,
    verbose=1
)
#%% 손실 및 정확도 변화 시각화
plt.plot(history.epoch, history.history["loss"], "bo", label="Training loss")
plt.plot(history.epoch, history.history["val_loss"], "r", label="Validation loss")
plt.title("Training and Validation loss")
plt.legend()
plt.show()

#%%
plt.plot(history.epoch, history.history["accuracy"], "bo", label="Training acc")
plt.plot(history.epoch, history.history["val_accuracy"], "r",
         label="Validation acc")
plt.title("Training and Validation accuracy")
plt.legend()
plt.show()

#%%
train_idg = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255.
)

train_dir_iterator = train_idg.flow_from_directory(
    train_path,
    target_size = (28,28),
    batch_size = 32,
    color_mode = "grayscale",
    class_mode = "categorical"
)
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), input_shape=(28, 28 ,1), activation="relu"),
    tf.keras.layers.MaxPool2D((2,2)),
    tf.keras.layers.Conv2D(64, (3,3), activation="relu"),
    tf.keras.layers.MaxPool2D((2,2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax")
])

model.compile(
    loss=tf.keras.losses.categorical_crossentropy,
    optimizer=tf.keras.optimizers.Adam(),
    metrics=["accuracy"]
)

history = model.fit_generator(
    train_dir_iterator,
    validation_data=val_dir_iterator,
    epochs=3,
    verbose=1
)
#%%
eval_result = model.evaluate_generator(
    test_dir_iterator
)
print("테스트 평가 결과:", eval_result)

#%%
print(eval_result)
#%%
import os
import cv2
import numpy as np

label_path = os.path.join(test_path, "2")
img_path = os.path.join(label_path, os.listdir(label_path)[0])
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
plt.imshow(img, cmap="gray")
plt.show()

img = img / 255.
img = img[np.newaxis, ..., np.newaxis]

result = model.predict_classes(img)
print(result)

#%%
model.save("model.h5")