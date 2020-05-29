from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D

base_model = MobileNetV2(weights = 'imagenet',input_shape = (200,200,3),include_top = False)

#Adding because mentioned in the tutorial
x = base_model.output
x = GlobalAveragePooling2D()(x)

#adding a fully connected layer
x = Dense(1024, activation = 'relu')(x)

#output layer
predictions = Dense(3,activation='softmax')(x)

model = Model(inputs = base_model.input, outputs = predictions)

#freezing the convolutional layers
for layer in base_model.layers:
    layer.trainable = False

#compiling the model
model.compile(optimizer = 'rmsprop', loss = 'categorical_crossentropy')

model.fit(df,y,epochs = 15,validation_split = 0.1)
model.predict(df[51].reshape(1,224,224,3)).argmax()


cap = cv2.VideoCapture(0)
while(True):
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    cv2.rectangle(frame, (400,100),(400+224,100+224),(0,255,0),3)
    fr = frame[100:324, 400:624]
    pred = model.predict(fr.reshape(1,224,224,3)).argmax()
    font = cv2.FONT_HERSHEY_SIMPLEX
    if(pred == 0):
        frame = cv2.putText(frame,'rock',(10,50),font,2,(0,0,255),1,cv2.LINE_AA)
    if(pred == 1):
        frame = cv2.putText(frame,'paper',(10,50),font,2,(0,0,255), 1,cv2.LINE_AA)
    if(pred == 2):
        frame = cv2.putText(frame,'scissors',(10,50),font,2,(0,0,255),1,cv2.LINE_AA)

    cv2.imshow('Frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()