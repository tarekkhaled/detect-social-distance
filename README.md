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

### Third Approach :
In this approach we used an API called openpose along with opencv and other image processing methods.

You could find a demo with some explanations and examples in this video: https://www.youtube.com/watch?v=d7-USTBZ8zE 

Openpose is an API which takes an image of people as input and turns the people into skeletons, the image is then sent to the jupyter notebook to measure the distance between the skeletons in the image.

You can download openpose API from this link: https://github.com/CMU-Perceptual-Computing-Lab/openpose

Here is an example:

Input
![Input](https://github.com/tarekkhaled/detect-social-distance/blob/master/Third%20Approach/ex1.png)

After downloading the openpose API, we put this image in the openpose/example/media folder and we open the windows command line in the root directory of the API and type this command:

bin\OpenPoseDemo.exe --image_dir examples\media\ --disable_blending --write_images folder_path

The output image will be saved in the corresponding path.

Output
![Output](https://github.com/tarekkhaled/detect-social-distance/blob/master/Third%20Approach/ex1_skeleton.png)  

The output image is then sent to this notebook: https://github.com/tarekkhaled/detect-social-distance/tree/master/Third%20Approach/Notebook

For this example the notebook will print the following output:
Distances from left to right: [49.598810916347155, 50.53764212000384, 51.64349988977317, 48.35040470618683]
Distances are in centimeters.

# Contributors 
[Alaa Atef](https://github.com/Alaa-Atef)
[Tarek Mohamed](https://github.com/Tarekmohamed97)
[Mostafa Emam](https://github.com/mostafaahmedemam)
[AbdEl Jalil Nasser](https://github.com/Abd-Eljalil-Nasser)

##### More information will be found in "proposal.pdf"
https://github.com/tarekkhaled/detect-social-distance/blob/master/proposal.pdf




