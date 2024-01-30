# raspberry-pi-5-mnist
Comparison of neural network training speed on raspberry pi 5 vs nvidia jetson nano - Mnist 


    I created a virtual Python environment using python3 -m venv neural.

    I installed the necessary packages for neural network training. (See the requirements.txt list).

    I found an example neural network project on the blog https://hedleyproctor.com/2020/12/jetson-nano-and-tensorflow/, which was executed and run on the Nvidia Jetson Nano. Here are the speeds during training:
    2020-12-30 11:46:56.368109: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1884] Adding visible gpu devices: 0
    2020-12-30 11:48:03.136928: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1428] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 22 MB memory) -> physical GPU (device: 0, name: NVIDIA Tegra X1, pci bus id: 0000:00:00.0, compute capability: 5.3)
    Epoch 1/5
    1875/1875 [==============================] - 17s 9ms/step - loss: 0.2918 - accuracy: 0.9158
    Epoch 2/5
    1875/1875 [==============================] - 17s 9ms/step - loss: 0.1385 - accuracy: 0.9584
    Epoch 3/5
    1875/1875 [==============================] - 16s 9ms/step - loss: 0.1049 - accuracy: 0.9678
    Epoch 4/5
    1875/1875 [==============================] - 17s 9ms/step - loss: 0.0864 - accuracy: 0.9733
    Epoch 5/5
    1875/1875 [==============================] - 16s 9ms/step - loss: 0.0738 - accuracy: 0.9774
    2020-12-30 11:51:36.564930: W tensorflow/core/framework/cpu_allocator_impl.cc:81] Allocation of 31360000 exceeds 10% of free system memory.
    313/313 - 2s - loss: 0.0733 - accuracy: 0.9774

    I ran the same network on the Raspberry Pi 5 and obtained:
    Epoch 1/5
    1875/1875 [==============================] - 10s 5ms/step - loss: 0.2971 - accuracy: 0.9133
    Epoch 2/5
    1875/1875 [==============================] - 8s 4ms/step - loss: 0.1425 - accuracy: 0.9578
    Epoch 3/5
    1875/1875 [==============================] - 8s 4ms/step - loss: 0.1061 - accuracy: 0.9677
    Epoch 4/5
    1875/1875 [==============================] - 8s 4ms/step - loss: 0.0868 - accuracy: 0.9727
    Epoch 5/5
    1875/1875 [==============================] - 8s 4ms/step - loss: 0.0740 - accuracy: 0.9764
    313/313 - 1s - loss: 0.0732 - accuracy: 0.9776 - 560ms/epoch - 2ms/step
    Summary:
    Total training time on the Raspberry: 42s
    Total training time on the Jetson: 83s
    Raspberry is 50% faster.
    Average training time per epoch on the Raspberry: 6.4s
    Average training time per epoch on the Jetson: 16.6s
    Raspberry is 2.5 times faster in each epoch.
