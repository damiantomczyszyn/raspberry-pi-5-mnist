#!/usr/bin/python3
 
import tensorflow as tf
 
# load standard sample data from the mnist dataset 1
# dataset 1 is images of the digits 0-9
mnist = tf.keras.datasets.mnist
 
# load both training and test data
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# the images have colour values from 0-255. these need to be scaled to be from 0-1
x_train, x_test = x_train / 255.0, x_test / 255.0
 
# now define our model
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])
 
predictions = model(x_train[:1]).numpy()
 
tf.nn.softmax(predictions).numpy()
 
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
 
loss_fn(y_train[:1], predictions).numpy()
 
model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])
 
model.fit(x_train, y_train, epochs=5)
 
model.evaluate(x_test,  y_test, verbose=2)
 
model(x_test[:5])
