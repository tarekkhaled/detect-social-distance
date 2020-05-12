# Detect-social-distance
Detect-social-distance is image processing project integrated with electron to slow the spread of coronavirus.

## Overview :
In our project, we want to help organizations to which a great number people go every day to monitor the distances between people in order to slow the spread of coronavirus.
These people stand in queues until their turn comes. These queues must not violate the social distancing rules.
Using a camera, a computer and image processing techniques we try to monitor the distances between people and release warnings if this distance is violated.

### More than one approch :
we have tried three different approchs .
every approch will be covered in detials . 


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

### Second  Approach :
In this approach we test images captured from camera and  use maskrcnn for object segmentation .

_Note :: for testing you should download mask_rcnn.h5 file from this link :https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5 , place it in approach2 folder  , check paths in notebook before running.

#### Idea :
we use mask rcnn for object segmentation , then check class and get coordinates for each object has class person.
then we compute all object heights and average of their height , and compare it with with average height of people (170cm)
now, we have ratio between real distance , and distance in image , so we calculate distance between objects in image and multiply with ratio we get real distance between all objects
then check distance if less than 1.8 m , we draw red boundary box  ,if more than 1.8m , draw green boundary box .

#### testcases and output :
Processing 1 images<br />
image                    shape: (653, 980, 3)         min:    0.00000  max:  255.00000  uint8 <br />
molded_images            shape: (1, 1024, 1024, 3)    min: -123.70000  max:  151.10000  float64 <br />
image_metas              shape: (1, 93)               min:    0.00000  max: 1024.00000  float64 <br />
anchors                  shape: (1, 261888, 4)        min:   -0.35390  max:    1.29134  float32 <br />
233.4390243902439 : 0   :  1 <br />
514.560975609756 : 0   :  2 <br />
682.9024390243902 : 0   :  3 <br />
281.1219512195122 : 1   :  2 <br />
449.4634146341463 : 1   :  3 <br />
168.34146341463415 : 2   :  3 <br />
![test 1 ](https://github.com/tarekkhaled/detect-social-distance/blob/master/output_4_1.png) <br />

Processing 1 images <br />
image                    shape: (675, 1200, 3)        min:    0.00000  max:  255.00000  uint8 <br />
molded_images            shape: (1, 1024, 1024, 3)    min: -123.70000  max:  151.10000  float64 <br />
image_metas              shape: (1, 93)               min:    0.00000  max: 1200.00000  float64 <br /> 
anchors                  shape: (1, 261888, 4)        min:   -0.35390  max:    1.29134  float32 <br /> 
183.5560344827586 : 0   :  1
406.0215517241379 : 0   :  2
222.4655172413793 : 1   :  2
![test 2 ](https://github.com/tarekkhaled/detect-social-distance/blob/master/output_4_3.png)

Processing 1 images
image                    shape: (500, 955, 3)         min:    0.00000  max:  255.00000  uint8
molded_images            shape: (1, 1024, 1024, 3)    min: -123.70000  max:  150.10000  float64
image_metas              shape: (1, 93)               min:    0.00000  max: 1024.00000  float64
anchors                  shape: (1, 261888, 4)        min:   -0.35390  max:    1.29134  float32
141.60241874527588 : 0   :  1
285.77475434618293 : 0   :  2
406.30385487528343 : 0   :  3
144.17233560090702 : 1   :  2
264.70143613000755 : 1   :  3
120.52910052910053 : 2   :  3

![test 3 ](https://github.com/tarekkhaled/detect-social-distance/blob/master/output_4_5.png)

Processing 1 images
image                    shape: (501, 752, 3)         min:    0.00000  max:  255.00000  uint8
molded_images            shape: (1, 1024, 1024, 3)    min: -123.70000  max:  151.10000  float64
image_metas              shape: (1, 93)               min:    0.00000  max: 1024.00000  float64
anchors                  shape: (1, 261888, 4)        min:   -0.35390  max:    1.29134  float32
310.3341584158416 : 0   :  1
605.940594059406 : 0   :  2
905.7549504950496 : 0   :  3
1337.0668316831684 : 0   :  4
295.6064356435644 : 1   :  2
595.4207920792079 : 1   :  3
1026.7326732673268 : 1   :  4
299.81435643564356 : 2   :  3
731.1262376237624 : 2   :  4
431.31188118811883 : 3   :  4
![test 4 ](https://github.com/tarekkhaled/detect-social-distance/blob/master/output_4_7.png)

Processing 1 images
image                    shape: (766, 1200, 3)        min:    0.00000  max:  255.00000  uint8
molded_images            shape: (1, 1024, 1024, 3)    min: -123.70000  max:  151.10000  float64
image_metas              shape: (1, 93)               min:    0.00000  max: 1200.00000  float64
anchors                  shape: (1, 261888, 4)        min:   -0.35390  max:    1.29134  float32
100.71663019693655 : 0   :  1
236.02844638949674 : 0   :  2
354.04266958424506 : 0   :  3
471.2199124726477 : 0   :  4
563.8457330415755 : 0   :  5
135.31181619256017 : 1   :  2
253.32603938730853 : 1   :  3
370.5032822757112 : 1   :  4
463.12910284463896 : 1   :  5
118.01422319474837 : 2   :  3
235.191466083151 : 2   :  4
327.8172866520788 : 2   :  5
117.17724288840263 : 3   :  4
209.8030634573304 : 3   :  5
92.6258205689278 : 4   :  5

![test 5 ](https://github.com/tarekkhaled/detect-social-distance/blob/master/output_4_9.png)

Processing 1 images
image                    shape: (957, 1300, 3)        min:    0.00000  max:  255.00000  uint8
molded_images            shape: (1, 1024, 1024, 3)    min: -123.70000  max:  151.10000  float64
image_metas              shape: (1, 93)               min:    0.00000  max: 1300.00000  float64
anchors                  shape: (1, 261888, 4)        min:   -0.35390  max:    1.29134  float32
38.871532453541604 : 0   :  1
73.89711823323458 : 0   :  2
108.51063829787233 : 0   :  3
141.88796121734447 : 0   :  4
172.51817936978185 : 0   :  5
35.02558577969297 : 1   :  2
69.63910584433073 : 1   :  3
103.01642876380285 : 1   :  4
133.64664691624023 : 1   :  5
34.613520064637754 : 2   :  3
67.99084298410988 : 2   :  4
98.62106113654725 : 2   :  5
33.37732291947212 : 3   :  4
64.0075410719095 : 3   :  5
30.63021815243738 : 4   :  5
![test 6 ](https://github.com/tarekkhaled/detect-social-distance/blob/master/output_4_11.png)

Processing 1 images
image                    shape: (867, 1300, 3)        min:    0.00000  max:  255.00000  uint8
molded_images            shape: (1, 1024, 1024, 3)    min: -123.70000  max:  151.10000  float64
image_metas              shape: (1, 93)               min:    0.00000  max: 1300.00000  float64
anchors                  shape: (1, 261888, 4)        min:   -0.35390  max:    1.29134  float32
52.325406381697775 : 0   :  1
105.6742925948224 : 0   :  2
156.72034918723662 : 0   :  3
209.81336544250453 : 0   :  4
53.34888621312463 : 1   :  2
104.39494280553885 : 1   :  3
157.48795906080676 : 1   :  4
51.04605659241421 : 2   :  3
104.13907284768213 : 2   :  4
53.09301625526792 : 3   :  4
![test 7 ](https://github.com/tarekkhaled/detect-social-distance/blob/master/output_4_13.png)

Processing 1 images
image                    shape: (353, 612, 3)         min:    0.00000  max:  255.00000  uint8
molded_images            shape: (1, 1024, 1024, 3)    min: -123.70000  max:  151.10000  float64
image_metas              shape: (1, 93)               min:    0.00000  max: 1024.00000  float64
anchors                  shape: (1, 261888, 4)        min:   -0.35390  max:    1.29134  float32
68.18596171376481 : 0   :  1
140.09115770282588 : 0   :  2
202.38833181403828 : 0   :  3
71.90519598906107 : 1   :  2
134.20237010027347 : 1   :  3
62.2971741112124 : 2   :  3
![test 8 ](https://github.com/tarekkhaled/detect-social-distance/blob/master/output_4_15.png)

Processing 1 images
image                    shape: (800, 1200, 3)        min:    0.00000  max:  255.00000  uint8
molded_images            shape: (1, 1024, 1024, 3)    min: -123.70000  max:  151.10000  float64
image_metas              shape: (1, 93)               min:    0.00000  max: 1200.00000  float64
anchors                  shape: (1, 261888, 4)        min:   -0.35390  max:    1.29134  float32
59.364250614250615 : 0   :  1
111.0534398034398 : 0   :  2
163.2125307125307 : 0   :  3
222.42014742014743 : 0   :  4
279.90479115479116 : 0   :  5
51.68918918918919 : 1   :  2
103.8482800982801 : 1   :  3
163.05589680589682 : 1   :  4
220.54054054054055 : 1   :  5
52.159090909090914 : 2   :  3
111.36670761670761 : 2   :  4
168.85135135135135 : 2   :  5
59.20761670761671 : 3   :  4
116.69226044226045 : 3   :  5
57.48464373464374 : 4   :  5
![test 9](https://github.com/tarekkhaled/detect-social-distance/blob/master/output_4_17.png)


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

# Output
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




