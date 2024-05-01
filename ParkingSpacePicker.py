import cv2

import pickle
# with the help of pickle we are store it created space of the image of parking 





width,height = 107,48
posList=[]

try:
    with open('example_imagePos' ,'rb') as f:
        posList=pickle.load(f);
except:
    poslist=[]

    

def mouseClick(events,x,y,flags,params):
    if events== cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events==cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(posList):
            x1,y1=pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)


    with open('example_imagePos','wb')as f:
        pickle.dump(posList,f)


while True:
    img=cv2.imread('example_image.png')

    # cv2.rectangle(img,(50,192),(157,240),(255,0,255),2)
    
    for pos in posList:
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255,0,255),2)

    cv2.imshow("Image",img)
    cv2.setMouseCallback("Image",mouseClick)
    cv2.waitKey(1)