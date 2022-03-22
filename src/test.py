#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
import time
import math


robot_width = .5
lidar_y_position = .1
clearence = .2
R_value = (robot_width/2)/math.sin(radians(22.5))+lidar_y_position+clearence

Wall_width = 3

def move_right():
	#may need to transform pose angle data
	pub = rospy.Publisher('twist_msg', Twist)
	msg = Twist()
    	linear_x = 0
    	angular_z = 0
    	state_description = ''
	# angular_z = 0.3 until fully turned
	if #Angle > -90:
		angular_z = 0.3
	else:
		a = msg.ranges[522.5:617.5]
		if min(a) <= R_value+clearence:
			Left = 2
		elif #x >= wall_width/2-clearence: 
			# lighthouse detects robot is too close to wall
			Left = 1
		else:
			Left = 0

		if Left == 2:
			state_description = 'Obstacle Detected'
			linear_x = 0.6
			angular_z = 0
		elif Left == 1:
			state_description = 'Too Close to Wall'
			#Turn straight, then run "move_left"
			if #Angle > 0:
				angular_z = -0.3
			else:
				move_left()
		elif Left == 0:
			state_description = 'Clear'
			if #Angle > 0:
				angular_z = -0.3
	rospy.loginfo(state_description)
    	msg.linear.x = linear_x
    	msg.angular.z = angular_z
    	pub.publish(msg)

def move_left():
	pub = rospy.Publisher('twist_msg', Twist)
	msg = Twist()
    	linear_x = 0
    	angular_z = 0
    	state_description = ''
	# angular_z = 0.3 until fully turned
	if #Angle < 90:
		angular_z = -0.3
	else:
		a = msg.ranges[522.5:617.5]
		if min(a) <= R_value+clearence:
			Right = 2
		elif #x >= wall_width/2-clearence: 
			# lighthouse detects robot is too close to wall
			Right = 1
		else:
			Right = 0

		if Right == 2:
			state_description = 'Obstacle Detected'
			linear_x = 0.6
			angular_z = 0
		elif Right == 1:
			state_description = 'Too Close to Wall'
			#Turn straight, then run "move_right"
			if #Angle > 0:
				angular_z = 0.3
			else:
				move_right()
		elif Right == 0:
			state_description = 'Clear'
			if #Angle > 0:
				angular_z = 0.3
	rospy.loginfo(state_description)
    	msg.linear.x = linear_x
    	msg.angular.z = angular_z
    	pub.publish(msg)

def move_straight():
	#may need to transform pose angle data
	pub = rospy.Publisher('twist_msg', Twist)
	msg = Twist()
    	linear_x = 0.6
    	angular_z = 0
    	state_description = 'Clear'
	rospy.loginfo(state_description)
    	msg.linear.x = linear_x
    	msg.angular.z = angular_z
    	pub.publish(msg)

def callback(msg):
   	a = msg.ranges[48:95]
    	if min(a) <= R_value:
        	Left = 1
    	else:
        	Left = 0
    	b = msg.ranges[0:47]
    	if min(b) <= R_value:
        	Front_left = 1
    	else:
        	Front_left = 0
    	c = msg.ranges[713:760]
    	if min(c) <= R_value:
        	Front_right = 1
    	else:
        	Front_right = 0
    	d = msg.ranges[665:713]
    	if min(d) <= R_value:
        	Right = 1
    	else:
        	Right = 0

#-------
    	pub = rospy.Publisher('twist_msg', Twist)
	msg = Twist()
    	linear_x = 0
    	angular_z = 0
    	state_description = ''
	if Left == 0 and Front_left == 0 and Front_right == 0 and Right == 0:
        	state_description = 'case 1 - clear'
       		move_straight()
        elif Left == 1 and Front_left == 0 and Front_right == 0 and Right == 0:
        	state_description = 'case 2 - far_left'
		move_right()
    	elif Left == 0 and Front_left == 1 and Front_right == 0 and Right == 0:
        	state_description = 'case 3 - front_left'
        	move_right()
        elif Left == 1 and Front_left == 1 and Front_right == 0 and Right == 0:
        	state_description = 'case 4 - left'
        	move_right()
        elif Left == 0 and Front_left == 0 and Front_right == 0 and Right == 1:
        	state_description = 'case 5 - far_right'
        	move_left()
    	elif Left == 0 and Front_left == 0 and Front_right == 1 and Right == 0:
        	state_description = 'case 6 - front_right'
        	move_left()
        elif Left == 0 and Front_left == 0 and Front_right == 1 and Right == 1:
        	state_description = 'case 7 - right'
        	move_left()
        elif Left == 0 and Front_left == 1 and Front_right == 1 and Right == 0:
        	state_description = 'case 8 - front'
        	move_right()
        elif Left == 1 and Front_left == 0 and Front_right == 0 and Right == 1:
        	state_description = 'case 9 - far_left/far_right'
        	move_left()
    	elif Left == 1 and Front_left == 0 and Front_right == 1 and Right == 0:
        	state_description = 'case 10 - far_left/front_right'
        	move_left()
        elif Left == 0 and Front_left == 1 and Front_right == 0 and Right == 1:
        	state_description = 'case 11 - front_left/far_right'
        	move_left()
        elif Left == 0 and Front_left == 1 and Front_right == 1 and Right == 1:
        	state_description = 'case 12 - front_left/right'
        	move_left()
        elif Left == 1 and Front_left == 1 and Front_right == 1 and Right == 0:
        	state_description = 'case 13 - left/front_right'
        	move_right()
        elif Left == 1 and Front_left == 0 and Front_right == 1 and Right == 1:
        	state_description = 'case 14 - far_left/right'
        	move_left()
    	elif Left == 1 and Front_left == 1 and Front_right == 0 and Right == 1:
        	state_description = 'case 15 - left/far_right'
        	move_left()
        elif Left == 1 and Front_left == 1 and Front_right == 1 and Right == 1:
        	state_description = 'case 16 - all_directions'
        	move_left()
        else:
        	state_description = 'unknown case'
    	print(state_description)


rospy.init_node('check_obstacle')

sub = rospy.Subscriber('/scan', LaserScan, callback)

rospy.spin()
