import pybullet as p
import time
import pybullet_data

# pip3 install pybullet
# pip3 install gym

pysicsClient = p.connect(p.GUI) #p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-9.81)

groundId = p.loadURDF("plane.urdf")
robotStartPos = [0,0,2]
robotStartOrientation = p.getQuaternionFromEuler([0,0,0])
robotId = p.loadURDF("grogu.urdf", robotStartPos, robotStartOrientation)

urdf = "/Users/shreeyapatel/School/robotics_studio/simulation/grogu.urdf"

for i in range(10000): 
    p.stepSimulation()
    # time.sleep(1./240.)
    time.sleep(1./1000.)
    robotPos, robotOrn = p.getBasePositionAndOrientation(robotId)
    print(robotPos, robotOrn)

p.disconnect()


