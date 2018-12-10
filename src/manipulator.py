#!/usr/bin/env python

import rospy
import roslib
import time
import math

from std_msgs.msg import String
from std_msgs.msg import Float64

from dynamixel_controllers.srv import SetTorqueLimit

pub = {}
command = {}
motorID = {}
val = {}
line_count
count = 1


def sendCommand(motorID, value):
    global  pub, set_torque

    #rospy.loginfo(motorID+':'+value)
    data = motorID + "," +value
    try:
        print('sendCommand ===> ' + str(motorID) + ' value: ' + str(value))
        value = float(value)
        if (motorID == 'gripper'):
            rospy.wait_for_service('/pan_controller_5/set_torque_limit')
            try:
                rospy.loginfo('setTorque')
                setTorque = rospy.ServiceProxy('/pan_controller_5/set_torque_limit', SetTorqueLimit)
                respTorque = setTorque(0.05)

            except rospy.ServiceException, e:
                print "Service Torque call failed"
            pass
        else:
            pass
        pub[motorID].publish(value)

    except ValueError:
        rospy.loginfo('Failed to sendCommand')
        if (motorID == 'gripper'):
            rospy.wait_for_service('/pan_controller_5/set_torque_limit')
            try:
                rospy.loginfo('setTorque')
                setTorque = rospy.ServiceProxy('/pan_controller_5/set_torque_limit', SetTorqueLimit)
                respTorque = setTorque(0.05)
            except rospy.ServiceException, e:
                print "Service Torque call failed"
        pub[motorID].publish(value)

    rospy.loginfo('#' + data)

def step():
    count = 1
    while count < line_count:
        sendCommand(motorID[str(count)],val[str(count)])
        count += 1

def main():

    #For Test
    motor = raw_input('name = ')
    pos = raw_input('pos = ')

    #Publisher
    global pub, set_torque
    pub['base'] = rospy.Publisher('/pan_controller_1/command', Float64, queue_size=10)
    pub['joint_1'] = rospy.Publisher('/pan_controller_2/command', Float64, queue_size=10)
    pub['joint_2'] = rospy.Publisher('/pan_controller_3/command', Float64, queue_size=10)
    pub['joint_3'] = rospy.Publisher('/pan_controller_4/command', Float64, queue_size=10)
    pub['gripper'] = rospy.Publisher('/pan_controller_5/command', Float64, queue_size=10)

    #Subscriber
    rospy.init_node('manipulator')

    #Status
    rospy.loginfo('Manipulator Start')
    sendCommand(motor, pos)
    rospy.spin()

if __name__ == '__main__':
    line_count = 1
    rospy.loginfo('Manipulator initial')
    file_name = raw_input('File name : ')
    try:
        file = open("action/"+file_name+".txt", "r")
        for line in file:
            command[line_count] = data
            line_count += 1
        while count < line_count:
            if count%2 != 0:
                motorID[str(count)] = command[count]
                count += 1
            else:
                val[str(count/2)] = command[count]
                count += 1

        main()
    except rospy.ROSInterruptException:
        pass
