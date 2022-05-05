#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from random import randint


def talker():
	pub = rospy.Publisher('dummy_odom', Odometry, queue_size = 1)
	rospy.init_node('dummy_odom', anonymous=True)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		msg = Odometry()
		pub.publish(msg)

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
