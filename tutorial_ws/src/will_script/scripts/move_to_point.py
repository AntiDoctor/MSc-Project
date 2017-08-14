#!/usr/bin/env python
# license removed for brevity
import rospy, time
from geometry_msgs.msg import PoseStamped

if __name__ == '__main__':
    # names this node created by script
    rospy.init_node('talker', anonymous=True)

    # MOVING THE TORSO
    # topic I'm publising to
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)

    nav_message = PoseStamped()
    nav_message.header.frame_id = 'map'
    nav_message.pose.position.x = 1
    nav_message.pose.position.y = -2
    nav_message.pose.position.z = 0

    nav_message.pose.orientation.x = 0.0
    nav_message.pose.orientation.y = 0.0
    nav_message.pose.orientation.z = 0
    nav_message.pose.orientation.w = 1

    time.sleep(2)
    pub.publish(nav_message)
