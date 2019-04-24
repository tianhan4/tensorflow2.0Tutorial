import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
print(tf.__version__)

def show_images(images, labels, class_names, predicts=None):
    if images.shape[0] > 9:
        print("Pls use less than 9 images for demonstration.")
        return
    fig, axes = plt.subplots(3, 3)
    fig.subplots_adjust(hspace=0.8, wspace=0.4)
    if len(labels.shape) > 1:
        labels = np.squeeze(labels)
    
    for i, ax in enumerate(axes.flat):
        if i >= images.shape[0]:
            ax.axis('off')
            continue
        ax.imshow(images[i])
        # Name of the true class.
        label_name = class_names[labels[i]]
        
        # Show true and predicted classes.
        if predicts is None:
            ax.set_xlabel("True : {0}".format(label_name))
        else:
            predict_name = class_names[predicts[i]]
            ax.set_xlabel("True: {0}\nPred: {1}".format(label_name, predict_name))
        # Remove ticks from the plot.
        ax.set_xticks([])
        ax.set_yticks([])
    plt.show()