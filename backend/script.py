#!/usr/bin/env python
# coding: utf-8


# In[1]:

import time
import numpy as np
import argparse
import sys
import cv2
from math import pow, sqrt
#print(os.getcwd())
import os
import sys
cwd = os.getcwd()
#time.sleep(60)

print(cwd)
#time.sleep(60)

#raw_input()

names_path=cwd+'/coco.names'
w_path=cwd+'/yolov3.weights'
cfg_path=cwd+'/yolov3.cfg'

#print(names_path,cfg_path,w_path)
#time.sleep(10)
with open(names_path, 'r') as f:
    classes = [line.strip() for line in f.readlines()]

    # generate different colors for different classes 
    COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

    # read pre-trained model and config file
    net = cv2.dnn.readNet(w_path,cfg_path )

cap = cv2.VideoCapture(0)
# function to get the output layer names 
# in the architecture
def get_output_layers(net):
    
    layer_names = net.getLayerNames()
    
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    return output_layers

# function to draw bounding box on the detected object with class name
def draw_bounding_box(img, class_id, confidence, x, y, x_plus_w, y_plus_h):

    label = str(classes[class_id])

    color = COLORS[class_id]

    cv2.rectangle(img, (x,y), (x_plus_w,y_plus_h), color, 2)

    cv2.putText(img, label, (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
def draw_bounding_box_v2(img, class_id, confidence, x, y, x_plus_w, y_plus_h,color):

    #label = str(classes[class_id])

    #color = COLORS[class_id]

    cv2.rectangle(img, (x,y), (x_plus_w,y_plus_h), color, 2)

    #cv2.putText(img, label, (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('D:/outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    # resize our captured frame if we need
    frame = cv2.resize(frame, None, fx=1.0, fy=1.0, interpolation=cv2.INTER_AREA)
    image=frame
    Width = image.shape[1]
    Height = image.shape[0]
    scale = 0.00392
    blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)

    # set input blob for the network
    net.setInput(blob)  
    
    

    # read class names from text file
    
    
    # function to get the output layer names 
# in the architecture
    

        # run inference through the network
    # and gather predictions from output layers
    outs = net.forward(get_output_layers(net))

    # initialization
    class_ids = []
    confidences = []
    boxes = []
    conf_threshold = 0.5
    nms_threshold = 0.4

    # for each detetion from each output layer 
    # get the confidence, class id, bounding box params
    # and ignore weak detections (confidence < 0.5)
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 :
                if class_id==0:
                    center_x = int(detection[0] * Width)
                    center_y = int(detection[1] * Height)
                    w = int(detection[2] * Width)
                    h = int(detection[3] * Height)
                    x = center_x - w / 2
                    y = center_y - h / 2
                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])

        # apply non-max suppression
    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)
    pos_dict = dict()
    coordinates = dict()
    # go through the detections remaining
    # after nms and draw bounding box
    for i in indices:
        i = i[0]
        box = boxes[i]
        x = box[0]
        y = box[1]
        w = box[2]
        h = box[3]

        draw_bounding_box(image, class_ids[i], confidences[i], round(x), round(y), round(x+w), round(y+h))
        F=615
        distance = (175 * F)/h
        print("Distance(cm):{dist}\n".format(dist=distance))
        x_cm = (x * distance) / F
        y_cm = (y * distance) / F
        pos_dict[i] = (x_cm,y_cm,distance)
    close_objects = set()
    for i in pos_dict.keys():
        for j in pos_dict.keys():
            if i < j:
                dist = sqrt(pow(pos_dict[i][0]-pos_dict[j][0],2) + pow(pos_dict[i][1]-pos_dict[j][1],2) + pow(pos_dict[i][2]-pos_dict[j][2],2))
                print(dist)
                # Check if distance less than 2 metres or 200 centimetres
                if dist < 200:
                    close_objects.add(i)
                    close_objects.add(j)
    for i in pos_dict.keys():
        if i in close_objects:
            COLOR = ([0,0,255])
        else:
            COLOR = ([0,255,0])
       # (startX, startY, endX, endY) = coordinates[i]
        #i = i[0]
        box = boxes[i]
        x = box[0]
        y = box[1]
        w = box[2]
        h = box[3]

        draw_bounding_box_v2(image, class_ids[i], confidences[i], round(x), round(y), round(x+w), round(y+h),COLOR)
        #cv2.rectangle(frame, (startX, startY), (endX, endY), COLOR, 2)
        #y = startY - 15 if startY - 15 > 15 else startY + 15
        # Convert cms to feet
        #cv2.putText(image, 'Depth: {i} ft'.format(i=round(pos_dict[i][2]/30.48,4)), (x, y),
           #        cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLOR, 2)
    # display o  
    cv2.namedWindow('Frame',cv2.WINDOW_AUTOSIZE)

    # Show frame
    #out.write(frame)

    cv2.imshow('Frame', frame)
    cv2.resizeWindow('Frame',800,600)

    key = cv2.waitKey(1) & 0xFF

    # Press `q` to exit
    if key == ord("q"):
        break

# Clean
cap.release()

raw_input()

cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




