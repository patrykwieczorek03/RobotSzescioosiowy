import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
import cv2
import urllib.request
import socket



url="http://192.168.1.150/capture"
#cv2.namedWindow("robot vision",cv2.WINDOW_AUTOSIZE)
image_counter=0
while True:
    imageResponse=urllib.request.urlopen(url)
    imgnp=np.array(bytearray(imageResponse.read()),dtype=np.uint8)
    img=cv2.imdecode(imgnp,-1)
    cv2.imshow("robot_vision",img)
    k = cv2.waitKey(1)
    if k%256 ==  32:
        img_name = "frame_{}.png".format(image_counter)
        cv2.imwrite(img_name,img)
        print("screen taken")
        image_counter += 1
        break
    #key=cv2.waitKey(5)
    #if key==ord('q'):
    #    break


path='C://Users//patry//Desktop//siecRobot//AI_predict//frame_0.png'

def load_image(path):
    img=image.load_img(path, target_size=(200,200))
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array,axis=0)
    img_batch /= 255.0
    plt.imshow(img_batch[0])
    plt.show()
    return img_batch


#url=https://script.google.com/macros/s/AKfycbwJQX867u9EOfZBU3RKK_e_dw4vjV1e_31ugpKBbfshhyW8J1Q/exec?square=1&circle=1&triangle=1&star=1
ksztalty=["kolo","kwadrat","gwiazda","trojkat"]
model=tf.keras.models.load_model('C://Users//patry//Desktop//siecRobot//robotAI')
pred=model.predict(load_image(path))
print(pred)
pred_val=np.argmax(pred)
print("ksztalt:",ksztalty[np.argmax(pred)])
s=socket.socket()
port=80
ip="192.168.1.151"
s.connect((ip,port))
if pred_val == 0:#dopasowane do kolejnosci na stm 0-kwadrat 1-kolo 2-trojkat 3-gwiazda
    message="1"
    s.send(message.encode())
    print("wyslano")
elif pred_val == 1:
    message="0"
    s.send(message.encode())
    print("wyslano")
elif pred_val == 2:
    message="3"
    s.send(message.encode())
    print("wyslano")
elif pred_val == 3:
    message="2"
    s.send(message.encode())
    print("wyslano")