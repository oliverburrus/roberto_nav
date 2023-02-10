#!/usr/bin/env python
# license removed for brevity
# Largely recycled from https://hotblackrobotics.github.io/en/blog/2018/01/29/action-client-py/
# https://automaticaddison.com/how-to-send-goals-to-the-ros-navigation-stack-using-c/

import rospy

# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
# So that we can subscribe to the tf
from geometry_msgs.msg import PoseStamped

def movebase_client(data):
    rospy.set_param('nav_to_mine', 0)

   # Get the goal wrt map frame (Is origin of map frame the location of the qr code??)
   # if map frame if where robot is initialized, we need to figure out the qr wrt goal minus the 
   # location of the qr code wrt robot
    position_x = data.pose.position.x
    position_y = data.pose.position.y
    orientation = data.pose.orientation.w

    goal_wrt_map_x = .5 - position_x #sample
    goal_wrt_map_y = .5 - position_y #sample
    orientation = 1 - orientation # figure out orientation wrt map frame

   # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
   # DO NOT UNDERSTAND WHAT AN ACTION SERVER IS AND IF WE HAVE ONE SET UP
    client.wait_for_server()

   # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "camera_odom_frame" 
    goal.target_pose.header.stamp = rospy.Time.now()
   # Move 0.5 meters forward along the x axis of the "map" coordinate frame 
    goal.target_pose.pose.position.x = goal_wrt_map_x
   # Move 0.5 meters forward along the y axis of the "map" coordinate frame 
    goal.target_pose.pose.position.y = goal_wrt_map_y
   # No rotation of the mobile base frame w.r.t. map frame
    goal.target_pose.pose.orientation.w = orientation

   # Sends the goal to the action server.
    client.send_goal(goal)
   # Waits for the server to finish performing the action.
    wait = client.wait_for_result()
   # If the result doesn't arrive, assume the Server is not available
    if not wait:
        rospy.logerr("Action server not available! Switch to manual control")
        rospy.signal_shutdown("Action server not available! Switch to manual control")
        # At this point manual override should commence. So should add that here.
    else:
    # Result of executing the action
        rospy.set_param('nav_to_mine', 1) #Trigger for mining script
        return client.get_result()   

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/object_22", PoseStamped, movebase_client)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        listener()
        result = movebase_client()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
