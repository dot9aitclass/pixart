import cv2
import numpy as np
k=int(raw_input("enter size of grid:"))
im=cv2.imread("laugh.jpg")
im=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
cv2.imshow('g',im)
cv2.waitKey()
w,h=np.size(im,0),np.size(im,1)
print w,h
vibgyor={1:[211, 0, 148],2:[130, 0, 75],3:[255, 0, 0],4:[0, 255, 0],5:[0, 255, 255],6:[0, 127, 255],7:[0, 0 , 255],8:[255,255,255],9:[0,0,0]}
#vibgyor={0:[255, 0, 0],1:[0, 127, 255],2:[255,255,255],3:[0,0,0]}
#for i in xrange(7):
    #print vibgyor[i]
vibhsv={1:[211, 0, 148],2:[130, 0, 75],3:[255, 0, 0],4:[0, 255, 0],5:[0, 255, 255],6:[0, 127, 255],7:[0, 0 , 255]}#8:[255,255,255],9:[0,0,0]}
for i in xrange(7):
    i=i+1
    a=np.uint8([[vibhsv[i]]])
    a=cv2.cvtColor(a,cv2.COLOR_BGR2HSV)
    vibhsv[i]=a[0][0]
    print vibhsv[i]
grid=np.full_like(im,255)
grid=cv2.cvtColor(grid,cv2.COLOR_BGR2HSV)
print grid
def gr(space,image):
    for y in xrange(w):
        if y%space==0:
            for x in xrange(h):
                image[y][x]=[0,0,0]
    for x in xrange(h):
        if x%space==0:
            for y in xrange(w):
                image[y][x]=[0,0,0]
#im=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
x=0
y=0
thresh=40
#print im
while x < w:
    y=0
    while y < h:
            #print 'y=',y
        #for i in xrange(7):
            """i=i+1
            bgr=vibgyor[i]
            minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
            maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])
    
            maskBGR = cv2.inRange(im,minBGR,maxBGR)
            resultBGR = cv2.bitwise_and(im, im, mask = maskBGR)
            cv2.imshow('g',resultBGR)
            cv2.waitKey()"""
            if im[x][y][0]==0 and im[x][y][1]==0 and im[x][y][2]!=0:
                if y+k<=h:
                    var=k
                else:
                    var=h-y      
                for ind in xrange(var):                       
                    im[x][y+ind]=[0,0,255]
            elif im[x][y][0]==0 and im[x][y][1]==0 and im[x][y][2]==0:
                if y+k<=h:
                    var=k
                else:
                    var=h-y                
                for ind in xrange(var):
                    im[x][y+ind]=[0,0,0]
            elif im[x][y][1]<15:
                if y+k<=h:
                    var=k
                else:
                    var=h-y      
                for ind in xrange(var):
                    im[x][y+ind]=[0,0,255]
            else:
                if im[x][y][0]>=140 and im[x][y][0]<255:
                    if y+k<=h:
                        var=k
                    else:
                        var=h-y      
                    for ind in xrange(var):                            
                        im[x][y+ind]=vibhsv[1]
                elif im[x][y][0]>=130 and im[x][y][0]<140:
                    if y+k<=h:
                        var=k
                    else:
                        var=h-y      
                    for ind in xrange(var):                            
                        im[x][y+ind]=vibhsv[2]
                elif im[x][y][0]>=70 and im[x][y][0]<130:
                    if y+k<=h:
                        var=k
                    else:
                        var=h-y      
                    for ind in xrange(var):
                        im[x][y+ind]=vibhsv[3]
                elif im[x][y][0]>=40 and im[x][y][0]<70:
                    if y+k<=h:
                        var=k
                    else:
                        var=h-y      
                    for ind in xrange(var):                            
                        im[x][y+ind]=vibhsv[4]
                elif im[x][y][0]>=20 and im[x][y][0]<40:
                    if y+k<=h:
                        var=k
                    else:
                        var=h-y      
                    for ind in xrange(var):
                        im[x][y+ind]=vibhsv[5]
                elif im[x][y][0]>=k and im[x][y][0]<20:
                    if y+k<=h:
                        var=k
                    else:
                        var=h-y      
                    for ind in xrange(var):                            
                        im[x][y+ind]=vibhsv[6]
                elif im[x][y][0]>=0 and im[x][y][0]<k:
                    if y+k<=h:
                        var=k
                    else:
                        var=h-y      
                    for ind in xrange(var):                            
                        im[x][y+ind]=vibhsv[7]
                    """elif im[x][y][0]==0 and im[x][y][1]==0  and im[x][y][2]==0:
                        for ind in xrange(var):
                            grid[x][y+ind]=[0,0,0]
                    elif im[x][y][1]>=150 and im[x][y][1]<=255  and im[x][y][2]>=200 and im[x][y][2]<=255: 
                        if im[x][y][0]>0 and im[x][y][0]<40:
                            for ind in xrange(var):
                                grid[x][y+ind]=[0,255,255]
                    elif im[x][y][1]==0 and im[x][y][2]==255:
                        for ind in xrange(var):
                            grid[x][y+ind]=[255,0,0]
                    elif im[x][y][0]==0 and im[x][y][1]==255:
                        for ind in xrange(var):
                            im[x][y+ind]=[0,255,255]"""                
            y=y+k+1
    x=x+1
    if x%k==0:
       x=x+1
    else:
       x=x

#ker=np.zeros((k,k,3))
im=cv2.cvtColor(im,cv2.COLOR_HSV2BGR)
#gr(k,im)
cv2.imshow('g',im)
cv2.waitKey()
#cv2.imwrite("newpixart.jpg",im)
