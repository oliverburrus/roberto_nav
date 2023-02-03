#!/usr/bin/env python
# license removed for brevity
# Largely recycled from https://hotblackrobotics.github.io/en/blog/2018/01/29/action-client-py/

import rospy

# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client():

   # Get the goal wrt map frame (Is origin of map frame the location of the qr code??)
   # if map frame if where robot is initialized, we need to figure out the qr wrt goal minus the 
   # location of the qr code wrt robot
    goal_wrt_map_x = .5 #sample
    goal_wrt_map_y = .5 #sample
    orientation = 1 # figure out orientation wrt map frame

   # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
   # DO NOT UNDERSTAND WHAT AN ACTION SERVER IS AND IF WE HAVE ONE SET UP
    client.wait_for_server()

   # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map" #I guess we can change the target frame.
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
        rospy.signal_shutdown("Action server not available!")
        # At this point manual override should commence. So should add that here.
    else:
    # Result of executing the action
        return client.get_result()   
        # Call the mining script
        # This could be done by publishing a sort of "completed task" signal which the 
        # mining script would depend upon and start when it publishes 1.

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")