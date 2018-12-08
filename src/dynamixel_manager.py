#!/usr/bin/env python

import rospy
import motor_01
import motor_02
import motor_03
import motor_04
import motor_05

__author__ = 'kanyajai'


def commander(motor, pos):

    if motor == '1':
        motor_01.command(pos)

    elif motor == '2':
        motor_02.command(pos)

    elif motor == '3':
        motor_03.command(pos)

    elif motor == '4':
        motor_04.command(pos)

    elif motor == '5':
        motor_05.command(pos)