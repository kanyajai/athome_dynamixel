#!/usr/bin/env python

import rospy
from dynamixel_manager import commander as arm_controller

from subprocess import call

__author__ = 'kanyajai'


"""
def real_commander(pos, motor):
    pos_string = str(pos)
    motor_string = str(motor)
    call("rostopic pub -1 /pan_controller_"+motor_string+"/command std_msgs/Float64 -- "+pos_string, shell=True)
    print("This is motor number : "+motor_string+" Position is : "+pos_string)
"""


def combo_motors(pos1, pos2, pos3, pos4, pos5):
    arm_controller('1', pos1)
    #rospy.sleep(3.2)
    arm_controller('2', pos2)
    #rospy.sleep(3.2)
    arm_controller('3', pos3)
    #rospy.sleep(3.2)
    arm_controller('4', pos4)
    #rospy.sleep(3.2)
    arm_controller('5', pos5)
    #rospy.sleep(3.2)


def hithere():
    while 1:
        pos = input("Pos = ")
        motor = raw_input("Motor = ")
        arm_controller(motor, pos)
        combo_motors(0, 0, 0, 0, 0)


if __name__ == '__main__':
    try:
        hithere()
    except rospy.ROSInterruptException:
        pass


