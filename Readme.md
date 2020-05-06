# Python installation and install required packages:
1. Download and install latest version of Python
2. Install the following packages
	openCV : run cmd 'pip install opencv-python'
	numpy : run cmd 'pip install numpy'

These two packages are required to display image data retrieved from simulator

# Steps to access simulator api in python(for windows):
1. Copy the following files to your working directory from 
	C:\Program Files\CoppeliaRobotics\CoppeliaSimEdu\programming\remoteApiBindings\python\python
	C:\Program Files\CoppeliaRobotics\CoppeliaSimEdu\programming\remoteApiBindings\lib\lib\Windows
	* sim.py
	* simConst.py
	* remoteApi.dll

2. Open given Demo.tt file

3. Copy/paste the following code to the script section of d420 bot in the Scene hierarchy
```lua
function sysCall_init() 
	simRemoteApi.start(19999)
end
```

4. Press Start/Resume Simulation in the simulator
5. Run Demo.py

### The minimum code requirements for python to connect to the simulator is available in Demo.py