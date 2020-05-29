import cv2
cap = cv2.VideoCapture(0)
irock = ipaper = iscissors =0;

while(True):
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    cv2.rectangle(frame, (400,100),(400+224,100+224),(0,255,0),3)
    cv2.imshow('Frame',frame)
    frame = frame[100:324, 400:624]
    #For rock
    if cv2.waitKey(1) & 0xFF == ord('r'):
        cv2.imwrite('rock/rock'+str(irock)+'.png',frame)
        irock+=1
        print(irock)
    #For paper
    if cv2.waitKey(1) & 0xFF == ord('p'):
        cv2.imwrite('paper/paper'+str(ipaper)+'.png',frame)
        ipaper+=1
        print(ipaper)
    #For scissors
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('scissors/scissors'+str(iscissors)+'.png',frame)
        iscissors+=1
        print(iscissors)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
