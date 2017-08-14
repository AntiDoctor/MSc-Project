#!/usr/bin/env python
import rospy, time
#from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from geometry_msgs.msg import WrenchStamped, Wrench, Vector3

def callback(msg):
    detector(msg)
    rospy.loginfo("Torque Force sensor output!")
    rospy.loginfo("Force Components: [%f, %f, %f]" % (msg.wrench.force.x, msg.wrench.force.y, msg.wrench.force.z))
    rospy.loginfo("Torque Components: [%f, %f, %f]" % (msg.wrench.torque.x, msg.wrench.torque.y, msg.wrench.torque.z))


def detector(msg):
    if (msg.wrench.force.x < -15):
        print ('object is 1kg')


if __name__ == '__main__':
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/wrist_ft", WrenchStamped, callback, queue_size=1)

    while (not rospy.is_shutdown()):
        time.sleep(0.2)
