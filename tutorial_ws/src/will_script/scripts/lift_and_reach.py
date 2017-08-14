#!/usr/bin/env python
# license removed for brevity
import rospy, time
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

if __name__ == '__main__':
	# names this node created by script	
	rospy.init_node('talker', anonymous=True)

	# MOVING THE TORSO	
	# topic I'm publising to
	pub = rospy.Publisher('/torso_controller/command', JointTrajectory, queue_size=10)

	torso_message = JointTrajectory()
	torso_message.joint_names = ['torso_lift_joint']
	torso_point = JointTrajectoryPoint()

	# raise up slightly
	torso_point.positions = [2]
	torso_point.time_from_start = rospy.Duration(1)
	torso_message.points.append(torso_point)

	time.sleep(2)
	pub.publish(torso_message)

	# MOVING THE ARM
	# topic I'm publising to
	pub = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=10)

	arm_message = JointTrajectory()
	arm_message.joint_names = ['arm_1_joint', 'arm_2_joint', 'arm_3_joint', 'arm_4_joint', 'arm_5_joint', 'arm_6_joint', 'arm_7_joint']
	arm_point = JointTrajectoryPoint()

	# home
	arm_point.positions = [0.2, -1.33, -0.2, 1.68, -1.52, 1.2, 1]
	arm_point.time_from_start = rospy.Duration(5)
	arm_message.points.append(arm_point)

	time.sleep(2)
	pub.publish(arm_message)
	time.sleep(6)

	# reach out
	arm_point.positions = [0.24, -1.42, -1.84, 1.66, -1.58, 0.08, 0]

	time.sleep(2)
	pub.publish(arm_message)
