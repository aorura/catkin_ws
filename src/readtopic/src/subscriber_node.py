#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose
from std_msgs.msg import Empty
import math

prevX=0
prevY=0
led_publisher = None

"""	if led_publisher is None:
		led_publisher = rospy.Publisher('/toggle_led', Empty, queue_size=10)
"""
def distance(x1, x2, y1, y2):
	#print ("dis: %lf\n" % ((x1-x2)**2 + (y1*10-y2*10)**2))
	#rospy.loginfo("px=%f py=%f x=%f y=%f" % (x1, x2, y1, y2))
	return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def callback(data):
	#rospy.loginfo("x=%f y=%f" % (data.x, data.y))
	global prevX
	global prevY
	global led_publisher

	dist = distance(prevX, data.x, prevY, data.y)

	#rospy.loginfo("%d : %d" % (prevX, prevY))
	if (dist > 1):
		rospy.loginfo("moved : %d" % (dist))
		prevX = data.x
		prevY = data.y

		led_msg = Empty()
		if not rospy.is_shutdown():
			led_publisher.publish(led_msg)
			rospy.spin()

def readtopic():
	rospy.init_node("turtlesim_listener", anonymous=True)
	rospy.Subscriber("/turtlesim1/turtle1/pose", Pose, callback)
	led_publisher = rospy.Publisher('/toggle_led', Empty, queue_size=10)

	rospy.spin()

if __name__ == "__main__":
	readtopic()
