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


## Usage
This is a brief introduction of tailoring Tensorflow 2.0Alpha for deep learning tasks. Some new features of Tensorflow 2.0Alpha are demonstrated here such as Eagle mode and integrated Keras. 

Some boxes in Eager.ipynb, KerasTraining.ipynb and RawTraining.ipynb are left blanked for you to fill as exercise for workshop. The complete solution is in 'solutins' folder.

The reading order should be as follows.

[Eager.ipynb](./Eager.ipynb) introduces basic operation of tensors and the difference between Eager mode and Graph mode in Tensorflow.

Data.ipynb is used for generating dataset for Tensorflow to use. You can use integrated pre-defined dataset or your own data.

Model.ipynb introduces three ways in Tensorflow to construct the same model. 

RawTraining.ipynb gives an example of training a model from scratch using raw Tensorflow functions.

KerasTraining.ipynb introduces how to perform training using Keras, which is more convenient.

Transfer_learning.ipynb introduces how to use pre-trained model on your own data to fine-tune a specific model.

