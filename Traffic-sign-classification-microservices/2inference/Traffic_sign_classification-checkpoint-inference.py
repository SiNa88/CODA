import cv2
import glob
import pickle
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
#import tensorflow.compat.v1 as tf 
#tf.disable_v2_behavior() 
#tf.compat.v1.disable_resource_variables()

model = load_model('traffic_sign_seq_highaccuracy.h5', compile = True)
model.summary()

file_name = "frame206.jpg"
IMG_SIZE = 32
img_array = cv2.imread(file_name ,cv2.IMREAD_GRAYSCALE)  
new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE), interpolation = cv2.INTER_AREA)
plt.imshow(new_array/255.0, cmap='gray')
plt.show()

#print (new_array.shape)
new_array_2 = np.reshape(new_array,(-1,32,32, 1))

#to predict single image
class_prob = model.predict(new_array_2.T, batch_size=1)
print(class_prob)
