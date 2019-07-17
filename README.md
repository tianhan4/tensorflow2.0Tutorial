# tensorflow2.0Tutorial

Python=3

## Installation
```
sudo apt-get install build-essential
pip install tensorflow==2.0.0-alpha0
pip install numpy
pip install matplotlib
pip install pillow

# Pls run this before distributing docker image to preload the data:
echo -e "from tensorflow import keras\nkeras.datasets.mnist.load_data()" | python
echo -e "from tensorflow import keras\nkeras.applications.VGG16(input_shape=(224,224,3), weights='imagenet',include_top=False)" | python
```
