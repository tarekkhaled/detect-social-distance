# Detect-social-distance
Detect-social-distance is image processing project integrated with electron to slow the spread of coronavirus.

## Overview :
In our project, we want to help organizations to which a great number people go every day to monitor the distances between people in order to slow the spread of coronavirus.
These people stand in queues until their turn comes. These queues must not violate the social distancing rules.
Using a camera, a computer and image processing techniques we try to monitor the distances between people and release warnings if this distance is violated.


### First Approach :
We use yolo3 for object detection , Yolo return boxes have (width, height) ,(center x , center y) for every boundary box .

'''
_Note :: for testing you should download (yolo3.weights) from this link: https://pjreddie.com/media/files/yolov3.weights , and locate it in approach1/backend , then open App.exe 
'''
#### Calibration :

```
Equation 1: focal length = (Z * p_h)/r_h
```
_Note :: Z: distance between camera and object , P_h : pixel height , r_h : actual height

focal length , it’s constant parameter for every camera (focal length of webcams around 615 ) 
from eq1 we compute focal length , by measure real distance between camera and object , actual height of object and pixel height (returned from yolo)
#### 
```
Equation 2 : Z = F * r_h / p_h

```
From Equation 2, We can compute distance between cam and each object 
_Note :: F (it’s constant) , pixel height (returned from yolo ) , we assume actual height of object = average height of person (165cm) 
Now we have Z for each object , (x , y) (from yolo) , by calculating Euclidean distance :
```
Distance between two objects = sqrt(pow(x1-x2,2)+pow(y1-y2,2)+pow(z1-z2,2))
```
Then , check if distance between objects less than 1.8 m , boundary box color change from green to red 

## Backend
We use [Jupyter Kernel Gateway](https://github.com/jupyter/kernel_gateway) to convert jupyter 
note book into a "REST API" and we use ......


### How to Install Jupyter Kernal Gateway ? _BACK-END_

_before below commands make sure you are in "pyhton/scripts" directory_
```
pip install jupyter_kernel_gateway
jupyter kernelgateway --generate-config
```


### How to Convert Jupyter notebook into REST API using Kernel Gateway ?
_opening notebook and then we will add_
```first cell
import json
```

```
# Imitate REQUEST args (with debugging time, usually ignore)
# REQUEST = json.dumps({'body': '', 'args': ''})
```
```
# GET /detect/social/distance/ /*This will make route for requesting it */

req = json.loads(REQUEST) /* REQUEST will be defiend globally by kernel gateway*/
args = req['args]

if 'start' not in args:
    print(json.dumps({'start':None}))
else:
    // OUr main Code
```

### How to running Jupyter notebook API ?
_before below commands make sure you are in "pyhton/scripts" directory_

```
jupyter kernelgateway --KernelGatewayApp.api='kernel_gateway.notebook_http' --KernelGatewayApp.seed_uri='./path of notebook like (notebook.ipynb)'

```

# Contributors 
[Alaa Atef](https://github.com/Alaa-Atef)
[Tarek Mohamed](https://github.com/Tarekmohamed97)
[Mostafa Emam](https://github.com/mostafaahmedemam)
[AbdEl Jalil Nasser](https://github.com/Abd-Eljalil-Nasser)

##### More information will be found in "proposal.pdf"
https://github.com/tarekkhaled/detect-social-distance/blob/master/proposal.pdf




