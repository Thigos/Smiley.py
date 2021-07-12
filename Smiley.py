import os
import cv2

diret = os.path.dirname(os.path.abspath(__file__))
face_cascade = cv2.CascadeClassifier(diret + '\\haarcascade\\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0) #Iniciar Cam (Padrão 0)
larguraCap, alturaCap = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while (True):
    rosto = cv2.imread(diret + '\\default.png')
    ret, frame = cap.read()

    if not ret:
    	break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 1)
    for (x, y, w, h) in faces:
        tl = (x,y) #Top Left
        br = (x + w, y + h) #X,Y Bottom Right


        rosto = cv2.imread(diret  + '\\Smiley.png')

        xCenter = int((tl[0]+br[0])/2)

        #olhoD = xCenter + 100
        #olhoE = xCenter - 100

        # if(xCenter < 200):
        # 	olhoE = 100
        # 	olhoD = 300
        # elif(xCenter > (larguraCap - 200)):
        # 	olhoD = (larguraCap - 100)
        # 	olhoE = (larguraCap - 300)

        #Espelhar Olhos

        olhoD = (larguraCap - xCenter) + 100
        olhoE = (larguraCap - xCenter) - 100

        if(xCenter < 200):
            olhoD = (larguraCap - 100)
            olhoE = (larguraCap - 300)
        elif(xCenter > (larguraCap - 200)):
        	olhoE = 100
        	olhoD = 300
        	

        cv2.rectangle(frame, tl,br, (80, 47, 245), 2)
        cv2.circle(frame, (xCenter, int((tl[1]+br[1])/2)) , 2, (0,0,255), 2)
        cv2.circle(frame, tl , 2, (0,255,0), 2)
        cv2.circle(frame, br , 2, (0,255,0), 2)
        cv2.circle(frame, (tl[0], br[1]) , 2, (0,255,0), 2)
        cv2.circle(frame, (br[0], tl[1]) , 2, (0,255,0), 2)

        print(xCenter, olhoD, olhoE)
        cv2.circle(rosto, (int(olhoD),150) , 50, (0,0,0), 2)
        cv2.circle(rosto, (int(olhoE),150) , 50, (0,0,0), 2)

        break

    cv2.imshow('Cam',frame)
    cv2.imshow('Rosto', rosto)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
