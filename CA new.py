# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:52:15 2019

@author: Z0040WMX
"""
import numpy as np 
import matplotlib.pyplot as plt
import cv2
import os
import time

path = 'C:\\Users\\Z0040WMX\\Desktop\\New folder (3)'
filesToRemove = [os.path.join(path,f) for f in os.listdir(path)]
for f in filesToRemove:
    os.remove(f) 

rows = int(input("Number of rows?"))
columns = int(input("Number of columns?"))
iteration = int(input("Number of iterations?"))

b = np.zeros((rows, columns))    
a = np.zeros((rows, columns))
timestr = time.strftime("%d_%m-%H_%M_%S")

#random matrix generator
#for i in range(0,rows):
#    for j in range(0,columns):    
#        random_number = np.random.random()
#        if random_number > 0.5:
#            a[i][j] = 0
#        else:
#            a[i][j] = 1
#    j = j+1
#i = i+1

#pre-defined matrix
a[1][25] = 1
a[2][25] = 1
a[2][23] = 1
a[3][22] = 1
a[3][21] = 1
a[3][35] = 1
a[3][36] = 1
a[3][13] = 1
a[3][14] = 1
a[4][12] = 1
a[4][16] = 1
a[4][21] = 1
a[4][22] = 1
a[4][35] = 1
a[4][36] = 1
a[5][1] = 1
a[5][2] = 1
a[6][1] = 1
a[6][2] = 1
a[5][11] = 1
a[6][11] = 1
a[7][11] = 1
a[8][12] = 1
a[9][13] = 1
a[9][14] = 1
a[6][15] = 1
a[8][16] = 1
a[5][17] = 1
a[6][17] = 1
a[7][17] = 1
a[6][18] = 1
a[6][23] = 1
a[6][25] = 1
a[7][25] = 1
a[5][21] = 1
a[5][22] = 1

#a[25][20] = 1
#a[25][21] = 1
#a[25][22] = 1
#a[25][23] = 1
#a[25][24] = 1
#a[25][25] = 1
#a[25][26] = 1
#a[25][27] = 1
#a[25][28] = 1
#a[25][29] = 1
#a[25][30] = 1

fig1 = plt.figure(figsize = (10, 20), edgecolor='b')
plt.imshow(a, vmin = 0, vmax = 1, cmap = 'binary')
plt.axis('image')
plt.title('Elementary Cellular Automaton', fontsize = 14)
plt.show()

for z in range(iteration): #iterates for n number of times
    
    for i in range(0,rows):
        for j in range(0,columns):
            m = 0
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                        if k < 0:
                            k = rows-1
                        elif k == rows:
                            k = 0
                        if l < 0:
                            l = columns - 1
                        elif l == columns:
                            l = 0
                        if k == i and l == j:
                            continue
                        elif a[k][l] == 1:
                            m = m + 1
                
            if m <2 and a[i][j] == 1:
                b[i][j] = 0
            elif m==2 and a[i][j] == 1:
                b[i][j] = 1
            elif m==3 and a[i][j] == 1: 
                b[i][j] = 1
            elif m>3 and a[i][j] == 1:
                b[i][j] = 0
            elif m ==3 and a[i][j] == 0:
                b[i][j] = 1

    fig1 = plt.figure(figsize = (10, 20))
    plt.imshow(b, vmin = 0, vmax = 1, cmap = 'plasma')
    plt.axis('image')
    plt.title('Elementary Cellular Automaton Rule {}'.format(z+1), fontsize = 14)
    plt.savefig('C:/Users/Z0040WMX/Desktop/New folder (3)/{}.jpg'.format(z+1))
    print('Current iteration = ', z, flush = True) 
    
    for p in range(rows):
        for q in range(columns):
            a[p][q] = b[p][q]
            
dir_name = os.listdir(path)

imagearray = []
res = []
filearray = []
img_array = []

for file in dir_name:
        imagearray.append(file)
            
res = sorted(imagearray, key=lambda x: int(x.split('.')[0]))

for counter in range(z+1):
    filecount = res[counter]
    filearray.append(os.path.join(path,filecount))
    
frame = cv2.imread(filearray[0])
height, width, layers = frame.shape
size = (width,height)

video = cv2.VideoWriter('C:/Users/Z0040WMX/Desktop/CA Videos/{}.avi'.format(timestr), 0, 10, (width,height))

for image in range(z+1):
    imag = filearray[image]
    video.write(cv2.imread(imag))

cv2.destroyAllWindows()
video.release()