#!/usr/bin/env python
import rospy
from subprocess import call

import grab_dynamixel
import commander
from dynamixel_msgs.msg import JointState
from std_msgs.msg import Float64


def resting_state():
    commander.combo_motors_2(0, 1.5, 2.2, 1.76, -0.65)


def pre_grab_state():
    commander.combo_motors_1(0, 1.5, 0, 0, -0.7)


def main():
    #resting_state()
    print("This is resting state")
    resting_state()
    call("espeak \"This is resting state\"", shell=True)
    rospy.sleep(5)
    print("This is pre-grab state")
    pre_grab_state()
    call("espeak \"This is pre grab state\"", shell=True)
    rospy.spin()


if __name__ == '__main__':
    main()
