#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from dynamixel_msgs.msg import JointState


def torque_limit(data):

    rospy.init_node('dynamixel_commander', anonymous=True)
    if data.load > -0.2:
            rospy.loginfo("Torque percentage = %s ", data.load)
            rospy.loginfo("Current pos = %s ", data.current_pos)
            x = data.current_pos
            x += 0.05
            commander(x)

    else:
            rospy.loginfo("STOP !!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            rospy.loginfo("Torque percentage = %s ", data.load * 100)
            commander(data.current_pos)
            STOP = 1


def commander(pos): # For give Position to dynamixel
    pub = rospy.Publisher('/tilt_controller_5/command', Float64, queue_size=10)
    rospy.init_node('dynamixel_commander', anonymous=True)
    pub.publish(pos)


def grab_state():

    rospy.loginfo("hello")
    rospy.init_node('dynamixel_commander', anonymous=True)
    rospy.Subscriber("/pan_controller_5/state", JointState, torque_limit)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    grab_state()
