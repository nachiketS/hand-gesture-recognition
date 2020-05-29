import pandas as pd
import numpy as np
import time
import cv2
df = []
y = []
for i in range(50):
    img = cv2.imread('rock/rock'+str(i)+'.png')
    df.append(img)
    y.append([1,0,0])
    # cv2.imshow("img",img)
    # time.sleep(1)
# cv2.imshow("img",img)
    print(np.array(df).shape)    

for i in range(50):
    img = cv2.imread('paper/paper'+str(i)+'.png')
    df.append(img)
    y.append([0,1,0])
    print(np.array(df).shape)    
for i in range(50):
    img = cv2.imread('scissors/scissors'+str(i)+'.png')
    df.append(img)
    y.append([0,0,1])
    print(np.array(df).shape)    
    
df = np.array(df)
y = np.array(y)   
print(df.shape)
# print(df)
# print(y)