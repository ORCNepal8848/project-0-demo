import sim
import sys
import cv2
import numpy as np
import time
#################################################################################### start conection to simulator
sim.simxFinish(-1) # just in case, close all opened connections
clientID = sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Get the client ID

if clientID!=-1:  #check if client connection successful
	print('Connected to remote API server')
else:
	print('Connection not successful')
	sys.exit('Could not connect')
##################################################################################### get reference to objects in simulator
errorCode, cameraHandle = sim.simxGetObjectHandle(clientID, 'Vision_sensor', sim.simx_opmode_oneshot_wait) # for camera
sim.simxGetVisionSensorImage(clientID, cameraHandle, 0, sim.simx_opmode_streaming) # start image streaming from camera sensor
errorCode, leftMotorHandle = sim.simxGetObjectHandle(clientID,'dr20_leftWheelJoint_',sim.simx_opmode_oneshot_wait)
errorCode, rightMotorHandle = sim.simxGetObjectHandle(clientID,'dr20_rightWheelJoint_',sim.simx_opmode_oneshot_wait)
  
while True: 
    returnCode, resolution, image = sim.simxGetVisionSensorImage(clientID, cameraHandle, 0, sim.simx_opmode_buffer)
    if returnCode == sim.simx_return_ok:
        img = np.array(image,dtype=np.uint8)
        img.resize([resolution[1],resolution[0],3])
        transformedImage = cv2.flip(img,0)
        transformedImage = cv2.cvtColor(transformedImage,cv2.COLOR_BGR2RGB)
        cv2.imshow('image',transformedImage)
        cv2.waitKey(1)
    elif returnCode == sim.simx_return_novalue_flag:
        print ('no image yet')
        pass
    errorCode=sim.simxSetJointTargetVelocity(clientID,leftMotorHandle,5, sim.simx_opmode_oneshot)
    errorCode=sim.simxSetJointTargetVelocity(clientID,rightMotorHandle,4.8, sim.simx_opmode_oneshot)