import numpy as np
import pandas as pd
import cv2

clicked = False
r = g = b = xpos = ypos = 0

image = cv2.imread("resources/colors.jpeg")
image=cv2.resize(image,(1400,700))
index=["color", "color_name", "hex", "R", "G", "B"]
data = pd.read_csv("C:/Users/Laptop/Downloads/colorcodes.csv", names=index, header=None,encoding='cp1252')
#print(data.head())
#cv2.imshow("Color",image)

def recognize_color(R,G,B):
    minimum = 10000
    for i in range(len(data)):
        d = abs(R- int(data.loc[i,"R"])) + abs(G- int(data.loc[i,"G"]))+ abs(B- int(data.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = data.loc[i,"color_name"]
    return cname

def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = image[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

cv2.namedWindow('Color Recognition App')
cv2.setMouseCallback('Color Recognition App', mouse_click)

while True:
    cv2.imshow("Color Recognition App",image)
    if (clicked):
        cv2.rectangle(image,(20,20), (1350,70), (b,g,r), -1)
        text = recognize_color(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        cv2.putText(image, text,(435,57),2,1,(255,255,255),2,cv2.LINE_AA)
        if(r+g+b>=600):
            cv2.putText(image, text,(435,57),2,1,(0,0,0),2,cv2.LINE_AA)
        clicked=False
    if cv2.waitKey(20) & 0xFF ==27:
        break

cv2.destroyAllWindows()

