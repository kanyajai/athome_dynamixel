#!/usr/bin/env python

import rospy

__author__ = 'kanyajai'

from std_msgs.msg import Float64


def command(pos):
    pub = rospy.Publisher('pan_controller_1_/command', Float64, queue_size=10)
    rospy.init_node('commander/motor_1', anonymous=True)
    pub.publish(pos)
        

