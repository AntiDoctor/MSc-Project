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

    # MOVING THE ARM
    # topic I'm publising to
    pub1 = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=10)

    arm_message = JointTrajectory()
    arm_message.joint_names = ['arm_1_joint', 'arm_2_joint', 'arm_3_joint', 'arm_4_joint', 'arm_5_joint', 'arm_6_joint',
                               'arm_7_joint']
    arm_point = JointTrajectoryPoint()

    # Return to home
    # set up arm messages
    # retract arm
    arm_point.positions = [0.2, -1.55, -0.2, 1.68, -1.52, 1.2, 1]
    arm_point.time_from_start = rospy.Duration(3)
    arm_message.points.append(arm_point)

    time.sleep(2)
    pub1.publish(arm_message)

    # lower torso
    torso_point.positions = [0.17]
    torso_point.time_from_start = rospy.Duration(1)
    torso_message.points.append(torso_point)

    time.sleep(2)
    pub.publish(torso_message)


    # Reach out
    #arm_point.positions = [0.24, -1.55, -1.84, 1.50, -1.58, 0.08, 0]

    time.sleep(1)

    # rise
    torso_point.positions = [0.35]

    time.sleep(2)
    pub.publish(torso_message)

    # reach
    arm_point.positions = [1.56, -0.98, -3.11, 1.04, -1.66, 0.05, 0.12]

    time.sleep(2)
    pub1.publish(arm_message)

    # lift
    time.sleep(2)

    arm_point.positions = [1.56, -0.98, -3.11, 1.5, -1.66, 0.05, 0.12]

    time.sleep(2)
    pub1.publish(arm_message)


    # OPEN AND CLOSE GRIPPERS
    # replace with ros service /gripper_controller/grasp
    # topic I'm publising to
    # code
    # pub = rospy.Publisher('/gripper_controller/command', JointTrajectory, queue_size=10)
    #
    # grip_message = JointTrajectory()
    # grip_message.joint_names = ['gripper_left_finger_joint', 'gripper_right_finger_joint']
    # grip_point = JointTrajectoryPoint()
    #
    # # open
    # grip_point.positions = [0.04, 0.04]
    # grip_point.time_from_start = rospy.Duration(1)
    # grip_message.points.append(grip_point)
    #
    # time.sleep(2)
    # pub.publish(grip_message)
    #
    # # grip
    # grip_point.positions = [0.02, 0.02]
    #
    # time.sleep(2)
    # pub.publish(grip_message)


