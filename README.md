# Detect-social-distance
Detect-social-distance is image processing project integrated with electron to slow the spread of coronavirus.

## Front-end
We use [electron](https://www.electronjs.org/) for GUI and communicating with Jupyter notebook with REST API for starting processing in backend 

### How to start electron app ? _GUI_

```
cd client/
npm install or yarn install 
npm start or yarn start

```
_Note :: config.js is responsible for REST API in electron_
_Note :: Make Sure the Jupyter notebook is running concurrently with GUI (FOR API)_

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


##### More information will be found in "proposal.pdf"
https://github.com/tarekkhaled/detect-social-distance/blob/master/proposal.pdf




