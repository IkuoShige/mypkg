import rclpy
from rclpy.node import Node
#from std_msgs.msg import Int16
#from person_msgs.msg import Person#add msg
from person_msgs.srv import Query

#"""
def cb(request, response):
    if request.name == "茂郁良":
        response.age = 44
    else:
        response.age = 255
    return response
#"""

rclpy.init()
node = Node("talker")
#pub = node.create_publisher(Int16, "countup", 10)
#pub = node.create_publisher(Person, "person", 10)#add msg
srv = node.create_service(Query, "query", cb)#add query
#n = 0

"""
def cb():
    global n
    #msg = Int16()
    msg = Person()#add msg
    msg.name = "茂郁良"#add msg
    #msg.data = n
    msg.age = n#add msg
    pub.publish(msg)
    n += 1
"""
#node.create_timer(0.5, cb)
rclpy.spin(node)
