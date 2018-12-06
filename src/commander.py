#!/usr/bin/env python

import rospy
from subprocess import call

__author__ = 'kanyajai'

from std_msgs.msg import Float64


def real_commander(pos, motor):
    pos_string = str(pos)
    motor_string = str(motor)
    call("rostopic pub -1 /pan_controller_"+motor_string+"/command std_msgs/Float64 -- "+pos_string, shell=True)
    print("This is motor number : "+motor_string+" Position is : "+pos_string)


def combo_motors_1(pos1, pos2, pos3, pos4, pos5):
    real_commander(pos1, 1)
    #rospy.sleep(3.2)
    real_commander(pos2, 2)
    #rospy.sleep(3.2)
    real_commander(pos3, 3)
    #rospy.sleep(3.2)
    real_commander(pos4, 4)
    #rospy.sleep(3.2)
    real_commander(pos5, 5)
    #rospy.sleep(3.2)


def combo_motors_2(pos1, pos2, pos3, pos4, pos5):
    real_commander(pos1, 1)
    #rospy.sleep(3.2)
    real_commander(pos2, 2)
    #rospy.sleep(3.2)
    real_commander(pos5, 5)
    #rospy.sleep(3.2)
    real_commander(pos4, 4)
    #rospy.sleep(3.2)
    real_commander(pos3, 3)
    #rospy.sleep(3.2)


def hithere():
    while 1:
        pos = raw_input("Pos = ")
        motor = raw_input("Motor = ")
        real_commander(pos, motor)


if __name__ == '__main__':
    try:
        hithere()
    except rospy.ROSInterruptException:
        pass


