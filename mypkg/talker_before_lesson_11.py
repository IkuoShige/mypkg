#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2022 Ikuo Shige                                                                                                           
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16 #lesson8
#from person_msgs.msg import Person#add msg
#from person_msgs.srv import Query#add query

"""
def cb(request, response):
    if request.name == "茂郁良":
        response.age = 44
    else:
        response.age = 255
    return response
#"""

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10) #lesson8
#pub = node.create_publisher(Person, "person", 10)#add msg
#srv = node.create_service(Query, "query", cb)#add query
n = 0

#"""#lesson8
def cb():
    global n
    msg = Int16()#lesson8
    #msg = Person()#add msg
    #msg.name = "茂郁良"#add msg
    msg.data = n#lesson8
    #msg.age = n#add msg
    pub.publish(msg)
    n += 1
#"""
node.create_timer(0.5, cb)#lesson8
rclpy.spin(node)
