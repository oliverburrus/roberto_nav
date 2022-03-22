#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import time
import math


robot_width = .5
lidar_y_position = .1
clearence = .2
R_value = (robot_width/2)/math.sin(radians(22.5))+lidar_y_position+clearence

Wall_width = 3

def move_right():
	pub = rospy.Publisher('twist_msg', Twist)
	msg = Twist()
    	linear_x = 0
    	angular_z = 0
    	state_description = ''
	# angular_z = 0.3 until fully turned
	if #Angle < 90:
		angular_z = 0.3
	else:
		a = msg.ranges[522.5:617.5]
		if min(a) <= R_value+clearence:
			Left = 2
		elif #y >= wall_width/2-clearence: 
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
				angular_z = 0.3
			else:
				move_left()
		elif Left == 0:
			state_description = 'Clear'
			if #Angle > 0:
				angular_z = 0.3
	rospy.loginfo(state_description)
    	msg.linear.x = linear_x
    	msg.angular.z = angular_z
    	pub.publish(msg)

def move_left():
	start_time = time.time()
	t1 = 3
	t2 = 6

	while True:
		current_time = time.time()
		elapsed_time = current_time - start_time
		
		if elapsed_time > t1:
			linear_x = 0.2
        		angular_z = -0.3

    			#msg.linear.x = linear_x
    			#msg.angular.z = angular_z
    			#pub.publish(msg)
		elif elapsed_time > t2:
			linear_x = 0.2
			angular_z = 0.3

    			#msg.linear.x = linear_x
    			#msg.angular.z = angular_z
    			#pub.publish(msg)

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
       		linear_x = 0.6
        	angular_z = 0
        elif Left == 1 and Front_left == 0 and Front_right == 0 and Right == 0:
        	state_description = 'case 2 - far_left'
        	linear_x = 0
        	angular_z = 0.3
    	elif Left == 0 and Front_left == 1 and Front_right == 0 and Right == 0:
        	state_description = 'case 3 - front_left'
        	linear_x = 0
        	angular_z = 0.3
        elif Left == 1 and Front_left == 1 and Front_right == 0 and Right == 0:
        	state_description = 'case 4 - left'
        	linear_x = 0
        	angular_z = 0.3
        elif Left == 0 and Front_left == 0 and Front_right == 0 and Right == 1:
        	state_description = 'case 5 - far_right'
        	linear_x = 0
        	angular_z = -0.3
    	elif Left == 0 and Front_left == 0 and Front_right == 1 and Right == 0:
        	state_description = 'case 6 - front_right'
        	linear_x = 0
        	angular_z = -0.3
        elif Left == 0 and Front_left == 0 and Front_right == 1 and Right == 1:
        	state_description = 'case 7 - right'
        	linear_x = 0
        	angular_z = -0.3
        elif Left == 0 and Front_left == 1 and Front_right == 1 and Right == 0:
        	state_description = 'case 8 - front'
        	linear_x = 0
        	angular_z = 0.3
        elif Left == 1 and Front_left == 0 and Front_right == 0 and Right == 1:
        	state_description = 'case 9 - far_left/far_right'
        	linear_x = 0
        	angular_z = -0.3
    	elif Left == 1 and Front_left == 0 and Front_right == 1 and Right == 0:
        	state_description = 'case 10 - far_left/front_right'
        	linear_x = 0
        	angular_z = -0.3
        elif Left == 0 and Front_left == 1 and Front_right == 0 and Right == 1:
        	state_description = 'case 11 - front_left/far_right'
        	linear_x = 0
        	angular_z = -0.3
        elif Left == 0 and Front_left == 1 and Front_right == 1 and Right == 1:
        	state_description = 'case 12 - front_left/right'
        	linear_x = 0
        	angular_z = -0.3
        elif Left == 1 and Front_left == 1 and Front_right == 1 and Right == 0:
        	state_description = 'case 13 - left/front_right'
        	linear_x = 0
        	angular_z = 0.3
        elif Left == 1 and Front_left == 0 and Front_right == 1 and Right == 1:
        	state_description = 'case 14 - far_left/right'
        	linear_x = 0
        	angular_z = -0.3
    	elif Left == 1 and Front_left == 1 and Front_right == 0 and Right == 1:
        	state_description = 'case 15 - left/far_right'
        	linear_x = 0
        	angular_z = -0.3
        elif Left == 1 and Front_left == 1 and Front_right == 1 and Right == 1:
        	state_description = 'case 16 - all_directions'
        	linear_x = 0
        	angular_z = -0.3
        else:
        	state_description = 'unknown case'
    	print(state_description)

    	rospy.loginfo(state_description)
    	msg.linear.x = linear_x
    	msg.angular.z = angular_z
    	pub.publish(msg)


rospy.init_node('check_obstacle')

sub = rospy.Subscriber('/scan', LaserScan, callback)

rospy.spin()
