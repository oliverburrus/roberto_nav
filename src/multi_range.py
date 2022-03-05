#!/usr/bin/env python

import rospy

from sensor_msgs.msg import LaserScan

R_value = .5

def callback(msg):
	a = msg.ranges[48:95]
	if min(a) <= R_value:
		print("A: 1")
	else:
		print("A: 0")
	b = msg.ranges[0:47]
	if min(b) <= R_value:
		print("B: 1")
	else:
		print("B: 0")
	c = msg.ranges[713:760]
	if min(c) <= R_value:
		print("C: 1")
	else:
		print("C: 0")
	d = msg.ranges[665:713]
	if min(d) <= R_value:
		print("D: 1")
	else:
		print("D: 0")


rospy.init_node('check_obstacle')

sub = rospy.Subscriber('/scan', LaserScan, callback)

rospy.spin()
