#!/usr/bin/env python

import rospy

__author__ = 'kanyajai'

from std_msgs.msg import Float64


def command(pos):
    pub = rospy.Publisher('/pan_controller_3/command', Float64, queue_size=10)
    rospy.init_node('commander_motor_3')
    pub.publish(pos)
    rospy.sleep(0.5)

def main():
    pos = input("Give me motor pos = ")
    command(pos)


if __name__ == '__main__':
    main()