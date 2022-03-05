#!/usr/bin/env python

import rospy

from sensor_msgs.msg import LaserScan

R_value = .5

def callback(msg):
	a = msg.ranges[40:50]
	if min(a) <= R_value:
		print("45deg: 1")
	else:
		print("45deg: 0")
	b = msg.ranges[62:72]
	if min(b) <= R_value:
		print("67.5deg: 1")
	else:
		print("67.5deg: 0")
	c = msg.ranges[85:95]
	if min(c) <= R_value:
		print("90deg: 1")
	else:
		print("90deg: 0")
	d = msg.ranges[107:117]
	if min(d) <= R_value:
		print("112.5deg: 1")
	else:
		print("112.5deg: 0")
	e = msg.ranges[130:140]
	if min(e) <= R_value:
		print("130deg: 1")
	else:
		print("130deg: 0")



rospy.init_node('check_obstacle')

sub = rospy.Subscriber('/scan', LaserScan, callback)

rospy.spin()
