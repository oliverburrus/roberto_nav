#!/usr/bin/env python  
#http://wiki.ros.org/tf/Tutorials/Writing%20a%20tf%20listener%20%28Python%29
import roslib
import rospy
import math
import tf
from geometry_msgs.msg import Pose


#meters
collection_bin_offset = 1

#initial_rotation = (math.pi/2)-(math.asin(0.46/pos)+#angle of depth cam to qr
                                          

        
if __name__ == '__main__':
    rospy.init_node('check_obstacle')

    listener = tf.TransformListener()

    pose_msg = rospy.Publisher('pose_msg', Pose ,queue_size=5)

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('camera_depth_frame', '/object_18', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        x = trans[0]
        y = trans[1]
        pos = math.sqrt(trans[0]**2+trans[1]**2)
        angular = math.atan2(trans[1], trans[0])
        pose = Pose()
        pose.position.x = x  #plus Imu_position_x
        pose.position.y = y - collection_bin_offset  #plus Imu_position_y
        pose.orientation.x = angular #plus Imu_rotation_from_y_axis
        pose_msg.publish(pose)
	print(pos)
        rate.sleep()
