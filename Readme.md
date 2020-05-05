Python installation procedure:
#todo
basic package opencv2 to display image

Steps to access simulator api in python:

Copy the following files to your working directory from 
	C:\Program Files\CoppeliaRobotics\CoppeliaSimEdu\programming\remoteApiBindings\python\python(for windows)
	C:\Program Files\CoppeliaRobotics\CoppeliaSimEdu\programming\remoteApiBindings\lib\lib\Windows(for windows)
1.sim.py
2.simConst.py
3.remoteApi.dll, remoteApi.dylib or remoteApi.so (depending on your target platform)

Open given Demo.tt file

Copy/paste the following code to the script section of d420 bot in the Scene hierarchy
function sysCall_init() 
	simRemoteApi.start(19999)
end

Press Start/Resume Simulation in the simulator
Then run Demo.py

The minimum code requirements for python to connect to the simulator is available in Demo.py