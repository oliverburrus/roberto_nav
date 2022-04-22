#!/usr/bin/env python  
#http://wiki.ros.org/tf/Tutorials/Writing%20a%20tf%20listener%20%28Python%29
import roslib
import rospy
import math
import tf
from geometry_msgs import PoseStamped
from sensor_msgs import Imu

#meters
collection_bin_offset = 1

initial_rotation = (math.pi/2)-(math.asin(0.46/pos)+#angle of depth cam to qr
                                          

        
def callback(Imu_data):
    if __name__ == '__main__':
            rospy.init_node('check_obstacle')

            listener = tf.TransformListener()

            pose_msg = rospy.Publisher('pose_msg', PoseStamped ,queue_size=5)

            rate = rospy.Rate(10.0)
            while not rospy.is_shutdown():
                try:
                    (trans,rot) = listener.lookupTransform('/tf', rospy.Time(0))
                except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                    continue

                x = trans[0]
                y = trans[1]
                pos = math.sqrt(trans[0]**2+trans[1]**2)
                angular = math.atan2(trans[1], trans[0])
                pose = PoseStamped()
                pose.position.x = x + #Imu_position_x
                pose.position.y = y - collection_bin_offset + #Imu_position_y
                pose.orientation.x = angular + #Imu_rotation_from_y_axis
                pose_msg.publish(pose)

                rate.sleep()



sub = rospy.Subscriber('/imu', Imu, callback)
rospy.spin()