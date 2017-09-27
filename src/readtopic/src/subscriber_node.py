#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose

def callback(data):
	rospy.loginfo("x=%f y=%f" % (data.x, data.y))

def readtopic():
	rospy.init_node("turtlesim_listener", anonymous=True)
	rospy.Subscriber("/turtle1/pose", Pose, callback)

	rospy.spin()

if __name__ == "__main__":
	readtopic()
