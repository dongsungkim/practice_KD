from keras.datasets import cifar10
import tensorflow as tf
import numpy as np

def get_cifar10():
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()#

    return (x_train, y_train), (x_test, y_test)

# train_data, test_data = get_cifar10()
# x_train, y_train = train_data
# x_test, y_test = test_data
#
# print (np.shape(x_train))
