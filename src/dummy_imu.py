#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu
from random import randint


def talker():
	pub = rospy.Publisher('dummy_imu', Imu, queue_size = 1)
	rospy.init_node('dummy_imu', anonymous=True)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		msg = Imu()
		pub.publish(msg)

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
