#!/usr/bin/env python

import rospy

__author__ = 'kanyajai'

from std_msgs.msg import Float64


def command(pos):
    rospy.init_node('commander_motor_2')
    pub = rospy.Publisher('/pan_controller_2/command', Float64, queue_size=10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(pos)
        rate.sleep()


def main():
    while 1:
        pos = input("Give me motor pos = ")
        command(pos)


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass