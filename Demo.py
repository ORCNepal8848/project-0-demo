import sim
import sys
import cv2
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

returnCode = 1
while returnCode !=0: 
    returnCode, resolution, image = sim.simxGetVisionSensorImage(clientID, cameraHandle, 0, sim.simx_opmode_buffer)
    print(returnCode)
    
while True: 
    returnCode, resolution, image = sim.simxGetVisionSensorImage(clientID, cameraHandle, 0, sim.simx_opmode_buffer)
    cv2.imshow('test',image)